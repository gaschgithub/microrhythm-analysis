# Microrhythm Analysis

This repository contains code and materials for the analysis of microrhythmic timing
deviations in symbolic music data (MIDI), developed as part of my undergraduate thesis
in Music and Artistic Technology (UNAM).

The project focuses on measuring inter-onset intervals (IOIs) in short rhythmic
fragments and expressing timing deviations as percentages relative to a nominal beat
duration at a given tempo.

## Microrhythm Analysis in Latin Popular Music

This repository contains analysis tools and data developed for my undergraduate thesis: "Microrhythms in Latin Popular Music: Quantification and Synthesis of Latin Sabor". The project focuses on the study of timing deviations at the sixteenth-note level using symbolic representations (MIDI) and inter-onset interval (IOI) analysis to compare rhythmic behaviors across genres.


## Project structure

```
microrhythm-analysis/
├── src/ # Analysis scripts
├── data/ # MIDI files and processed data
├── notebooks/ # Exploratory analysis and visualizations
├── figures/ # Plots and exported figures
```

## Methods (overview)

- Perceptual identification and manual encoding of rhythmic events as MIDI sequences (16-beat excerpts).
- MIDI parsing and extraction of onset times.
- Computation of inter-onset intervals (IOI) in milliseconds.
- Normalization of timing deviations relative to tempo (BPM).
- Export of results for statistical and comparative analysis.

## Technologies

- Python
- MIDI processing libraries
- NumPy / Pandas / Matplotlib

## Status

Work in progress...
