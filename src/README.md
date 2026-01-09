## Analysis Modules

This directory contains Python modules used for symbolic microrhythm analysis, covering both MIDI-based IOI extraction and Excel-based statistical analysis and visualization.

### Modules

- `ioi_analysis.py`: Extraction of onset times and inter-onset intervals (IOI) from MIDI files, including beat subdivision analysis and export to Excel.
- `excel_analysis_std.py`: Statistical analysis and visualization of microrhythmic duration data exported to Excel, including mean values and standard deviation.

### Dependencies

- Python 3.9+
- mido
- pandas
- xlrd
- matplotlib

### Notes

- The analysis assumes a constant tempo provided by the user.
- MIDI files are expected to contain manually curated rhythmic events.
- Default analysis length is 16 beats (4 bars of 4/4).
- Some genres (e.g., Brazilian funk) may exhibit variable beat subdivision (3 or 4), which must be specified during statistical analysis and visualization.



