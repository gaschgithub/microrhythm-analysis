# Data

This folder contains the datasets used in the microrhythm analysis project.

## Files

### `Mediciones_Microrritmos.xlsx`
Master dataset containing all microrhythmic measurements extracted from manually encoded MIDI files.
Each row corresponds to a measured rhythmic event within a 16-beat excerpt.
This file is used as input for both `excel_analysis_std` and `excel_analysis` scripts.

### `corpus.md`
List of musical excerpts analyzed in this study, organized by genre.
Each entry corresponds to a manually encoded MIDI excerpt used for timing analysis.

### MIDI corpus
`data/MIDI templates/` contains manually encoded MIDI files (16-beat excerpts),
organized by genre:

- cumbia
- salsa
- joeson
- bossa
- funk_brasileiro

Each MIDI file represents perceptually identified rhythmic events,
encoded manually in a DAW prior to IOI extraction.

## Notes

- All analyses assume a constant tempo per excerpt, provided by the user.
