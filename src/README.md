## IOI Analysis Module

This module provides utilities for extracting inter-onset intervals (IOI) from MIDI files and organizing microrhythmic timing data for analysis.

### Functions

- `process_midi_file`: Extracts onset times and inter-onset intervals from a MIDI file.
- `determine_subdivisions_per_beat`: Computes the number of rhythmic subdivisions per beat.
- `export_ioi_to_excel`: Exports IOI data to an Excel file for further analysis.

### Dependencies

- Python 3.9+
- mido
- pandas

### Notes

- The module assumes a constant tempo provided by the user.
- MIDI files are expected to contain manually curated rhythmic events.
- Default analysis length is 16 beats (4 bars of 4/4).
