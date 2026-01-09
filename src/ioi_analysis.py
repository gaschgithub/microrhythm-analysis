"""
Microrhythm IOI analysis utilities.

This module extracts inter-onset intervals (IOI) from manually encoded
MIDI files and organizes microrhythmic timing data for further analysis.
Beat-level subdivisions are inferred automatically from onset distribution.
"""

import mido
import pandas as pd


# ---------- CONFIGURATION ----------
NUM_BEATS = 16          # Default analysis length (16 beats = 4 bars of 4/4)
PRECISION_TOLERANCE = 1e-6


# ---------- MIDI PROCESSING ----------
def process_midi_file(midi_file_path, tempo_bpm):
    """
    Extract onset times and inter-onset intervals (IOI) from a MIDI file.

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
    total_duration_ms = beat_duration_ms * NUM_BEATS

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


# ---------- SUBDIVISION DETECTION ----------
def determine_subdivisions_per_beat(onsets, tempo_bpm, num_beats=NUM_BEATS):
    """
    Infer the number of rhythmic subdivisions per beat based on onset density.

    This function allows beats to contain varying numbers of subdivisions
    (e.g., 3, 4, or alternating patterns), which is particularly relevant
    for genres such as Brazilian funk.

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
        Number of detected subdivisions per beat.
    """
    beat_duration_ms = (60 / tempo_bpm) * 1000
    subdivisions = []

    for beat_index in range(num_beats):
        beat_start = beat_index * beat_duration_ms
        beat_end = (beat_index + 1) * beat_duration_ms - PRECISION_TOLERANCE

        onsets_in_beat = [
            onset for onset in onsets
            if beat_start <= onset < beat_end
            or abs(onset - beat_start) < PRECISION_TOLERANCE
        ]

        subdivisions.append(len(onsets_in_beat))

    return subdivisions


# ---------- EXCEL EXPORT ----------
def export_ioi_to_excel(iois, subdivisions, tempo_bpm, output_path):
    """
    Export IOI data to an Excel file with adaptive beat subdivision handling.

    Each row corresponds to one beat. Beats with fewer than four subdivisions
    are zero-padded with empty cells to ensure a consistent table structure.

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
