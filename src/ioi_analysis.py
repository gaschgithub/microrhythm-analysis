"""
Microrhythm IOI analysis utilities.

This module provides functions to extract inter-onset intervals (IOI)
from MIDI files and organize microrhythmic timing data for analysis.
"""

import mido
import pandas as pd


def process_midi_file(midi_file_path, tempo_bpm):
    """
    Process a MIDI file to compute onset times and inter-onset intervals (IOI).

    Parameters
    ----------
    midi_file_path : str
        Path to the MIDI file.
    tempo_bpm : float
        Tempo in beats per minute.

    Returns
    -------
    iois : list of float
        Inter-onset intervals in milliseconds.
    onsets : list of float
        Onset times in milliseconds.
    """
    midi = mido.MidiFile(midi_file_path)
    beat_duration_ms = (60 / tempo_bpm) * 1000
    total_duration_ms = beat_duration_ms * 16  # 16 beats (4 bars of 4/4)

    onsets = []
    current_time = 0.0

    for track in midi.tracks:
        for msg in track:
            if msg.time > 0:
                current_time += msg.time * (beat_duration_ms / midi.ticks_per_beat)
                onsets.append(current_time)

    if 0.0 not in onsets:
        onsets.insert(0, 0.0)

    onsets = sorted(onsets)
    iois = [onsets[i + 1] - onsets[i] for i in range(len(onsets) - 1)]

    if onsets:
        iois.append(total_duration_ms - onsets[-1])

    return iois, onsets


def determine_subdivisions_per_beat(onsets, tempo_bpm, num_beats=16):
    """
    Determine the number of rhythmic subdivisions per beat.

    Parameters
    ----------
    onsets : list of float
        Onset times in milliseconds.
    tempo_bpm : float
        Tempo in beats per minute.
    num_beats : int
        Number of beats to analyze.

    Returns
    -------
    subdivisions : list of int
        Number of onsets per beat.
    """
    beat_duration_ms = (60 / tempo_bpm) * 1000
    precision_tolerance = 1e-6

    subdivisions = []

    for beat_index in range(num_beats):
        beat_start = beat_index * beat_duration_ms
        beat_end = (beat_index + 1) * beat_duration_ms - precision_tolerance

        onsets_in_beat = [
            onset for onset in onsets
            if beat_start <= onset < beat_end
            or abs(onset - beat_start) < precision_tolerance
        ]

        subdivisions.append(len(onsets_in_beat))

    return subdivisions


def export_ioi_to_excel(iois, subdivisions, tempo_bpm, output_path):
    """
    Export IOI data to an Excel file with dynamic subdivision handling.

    Parameters
    ----------
    iois : list of float
        Inter-onset intervals in milliseconds.
    subdivisions : list of int
        Number of subdivisions per beat.
    tempo_bpm : float
        Tempo in beats per minute.
    output_path : str
        Output Excel file path.
    """
    beat_duration_ms = (60 / tempo_bpm) * 1000
    data = []
    iois_index = 0

    for num_subdivisions in subdivisions:
        row_ms = []
        row_pct = []

        for _ in range(num_subdivisions):
            if iois_index < len(iois):
                value_ms = iois[iois_index]
                row_ms.append(value_ms)
                row_pct.append((value_ms / beat_duration_ms) * 100)
                iois_index += 1

        while len(row_ms) < 4:
            row_ms.append(None)
            row_pct.append(None)

        data.append(row_ms[:4] + row_pct[:4])

    columns = [
        "1 (ms)", "2 (ms)", "3 (ms)", "4 (ms)",
        "1 (%)", "2 (%)", "3 (%)", "4 (%)"
    ]

    df = pd.DataFrame(data, columns=columns)
    df.to_excel(output_path, index=False)
