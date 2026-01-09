# Microrhythm Analysis

This repository contains code and materials for the analysis of microrhythmic timing
deviations in symbolic music data (MIDI), developed as part of my undergraduate thesis
in Music and Artistic Technology (UNAM).

The project focuses on measuring inter-onset intervals (IOIs) in short rhythmic
fragments and expressing timing deviations as percentages relative to a nominal beat
duration at a given tempo.

## Project structure

microrhythm-analysis/
├── src/ # Analysis scripts
├── data/ # MIDI files and processed data
├── notebooks/ # Exploratory analysis and visualizations
├── figures/ # Plots and exported figures

## Methods (overview)

- MIDI parsing and onset extraction
- IOI computation in milliseconds
- Normalization relative to tempo (BPM)
- Export of results for statistical analysis

## Technologies

- Python
- MIDI processing libraries
- NumPy / Pandas / Matplotlib

## Status

Work in progress...
