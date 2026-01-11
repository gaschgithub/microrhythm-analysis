# Analysis Modules

This directory contains Python modules used for symbolic microrhythm analysis, covering
MIDI-based IOI extraction as well as Excel-based statistical analysis and visualization.

## Modules

### `ioi_analysis.py`
Extraction of onset times and inter-onset intervals (IOI) from manually encoded MIDI files.
Beat-level subdivisions are **inferred automatically** from onset distribution, allowing
for variable subdivision patterns (e.g., alternating 3- and 4-part subdivisions).
Results are exported to Excel for subsequent analysis.

### `excel_analysis_std.py`
Statistical analysis of microrhythmic duration data exported to Excel.
Computes mean values and frequency-weighted standard deviation, and generates scatter plots
to visualize duration distributions at the subdivision level.
The number of subdivisions per beat (3 or 4) is specified explicitly by the user.

### `excel_analysis.py`
Visualization of microrhythmic timing for individual musical excerpts.
Plots the duration of each subdivision across the 16 analyzed beats of a single song,
based on data extracted from the aggregated Excel dataset.
The number of subdivisions per beat (3 or 4) is specified explicitly by the user.

### `excel_genre_comparison.py`
Cross-genre comparison of average sixteenth-note (four-subdivision) durations. Generates a three-dimensional visualization to compare microrhythmic profiles across selectable 2-5 genres.

## Dependencies

- Python 3.9+
- mido
- pandas
- xlrd
- matplotlib

## Notes

- The analysis assumes a constant tempo provided by the user.
- MIDI files are expected to contain manually curated rhythmic events derived from perceptual listening.
- Default analysis length is 16 beats (4 bars of 4/4).
- While most analyzed genres exhibit a consistent four-part subdivision of the beat,
  Brazilian funk excerpts may present three-part or alternating subdivision patterns.
  Automatic subdivision detection is performed at the MIDI analysis stage, while
  subdivision count is specified manually during Excel-based analysis and visualization.
