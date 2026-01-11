# Microrhythm Analysis

This repository contains the data, analysis scripts, and figures developed for my
undergraduate thesis in Music and Artistic Technology (UNAM):

**_Microrhythms in Latin Popular Music: Quantification and Synthesis of Latin Sabor_**

The project investigates **systematic microrhythmic timing deviations** in selected
Latin popular music genres, using **symbolic representations (MIDI)** derived from
perceptually identified rhythmic events. Timing deviations are quantified through
inter-onset interval (IOI) analysis and expressed as percentages relative to a nominal
beat duration at a fixed tempo.

This repository is conceived as a **research system**, prioritizing methodological
clarity, inspectability, and reproducibility over automation or large-scale processing.

---

## Research focus

Microrhythm is treated here not as performance imprecision, but as a **structural and
expressive component of groove**, closely linked to style, embodied musical knowledge,
and long-term performance practice.

The central research questions addressed by this project are:

- How are microrhythmic timing deviations distributed within the beat across different
  Latin popular music genres?
- Do these deviations exhibit **systematic, genre-specific patterns** rather than
  random variability?
- Can symbolic microrhythmic measurements reveal stylistic proximity or distance
  between genres that share historical or cultural roots?

The study adopts a **comparative, subdivision-level perspective**, focusing on short
rhythmic fragments in order to preserve perceptual grounding while enabling precise
temporal measurement.

---

## Corpus and genres

The corpus consists of **manually encoded 16-beat MIDI excerpts**, each representing a
short rhythmic fragment extracted from a recorded performance. The following genres
are included in the dataset published in this repository:

- Salsa  
- Cumbia  
- Joesón (Colombian salsa style associated with Joe Arroyo)  
- Bossa Nova  
- Brazilian Funk  

All rhythmic events were **identified perceptually** and encoded manually prior to
analysis. No automatic onset detection was used.

A complete list of analyzed excerpts is provided in `data/corpus.md`.

> **Note:** While the written thesis discusses a broader stylistic context, this
> repository contains the finalized microrhythmic dataset used for quantitative
> analysis and figure generation.

---

## Methodological overview

The analysis pipeline implemented in this repository follows these steps:

1. **Perceptual identification** of salient rhythmic events in recorded performances.
2. **Manual encoding** of these events as MIDI sequences (16-beat excerpts).
3. **Extraction of onset times** from MIDI files.
4. **Computation of inter-onset intervals (IOIs)** in milliseconds.
5. **Inference of beat subdivisions** from onset distributions.
6. **Normalization of timing deviations** relative to the nominal beat duration.
7. **Statistical analysis and visualization** at the subdivision level.

Symbolic representations are used deliberately to allow for precise timing analysis
and explicit control over rhythmic structure, at the cost of excluding timbral and
micro-dynamic dimensions.

---

### Subdivision modeling

Most analyzed genres exhibit a consistent **four-part subdivision of the beat**
(corresponding to sixteenth notes). However, Brazilian funk excerpts may alternate
between **three- and four-part subdivisions**, sometimes within the same musical
fragment.

This variability is handled explicitly:

- Subdivision structure is **automatically inferred** during IOI extraction.
- Statistical analysis and visualization scripts require the user to specify whether
  **3 or 4 subdivisions per beat** are assumed.
- In the case of three subdivisions, the term **“twelfth notes”** is used for analytical
  consistency.
- For cross-genre comparison, only funk excerpts with **four detected subdivisions**
  are included.

---

## Key findings (thesis summary)

Cross-genre comparison of average subdivision durations suggests the emergence of
**stylistic clusters**:

- **Salsa and Joesón** exhibit the closest microrhythmic similarity, consistent with
  their shared derivation from son-based rhythmic organization.
- **Cumbia** appears closer to Salsa/Joesón than to Brazilian genres, plausibly
  reflecting Caribbean rhythmic influence and a shared treatment of off-beat timing.
- **Bossa Nova and Brazilian Funk** form a more distant group relative to the above,
  showing tendencies associated with samba-derived practices and, in the case of funk,
  subdivision alternation.

These results support the hypothesis that microrhythmic duration patterns can reflect
tacit stylistic consensus across genres, even when not codified as explicit rules.

---

## Repository structure

```
├── src/ # Analysis scripts
├── data/ # MIDI corpus and aggregated measurement data
├── figures/ # Curated figures generated from the analysis
├── README.md
├── requirements.txt
└── LICENSE
```

---

## Source code (`src/`)

- `ioi_analysis.py`  
  Extraction of onset times and inter-onset intervals (IOIs) from manually encoded MIDI
  files. Beat-level subdivisions are inferred automatically from onset distributions.
  Results are exported to Excel for subsequent analysis.

- `excel_analysis_std.py`  
  Statistical analysis of microrhythmic duration data exported to Excel. Computes mean
  values and frequency-weighted standard deviation, and generates scatter plots to
  visualize duration distributions at the subdivision level. The number of
  subdivisions per beat (3 or 4) is specified explicitly by the user.

- `excel_analysis.py`  
  Visualization of microrhythmic timing for individual musical excerpts. Plots the
  duration of each subdivision across the 16 analyzed beats of a single song, based on
  data extracted from the aggregated Excel dataset.

- `excel_genre_comparison.py`  
  Cross-genre comparison of average sixteenth-note (four-subdivision) durations.
  Generates a three-dimensional visualization used in the thesis conclusion to compare
  microrhythmic profiles across genres. Includes a configuration section allowing the
  user to select and order 2–5 genres. Brazilian funk excerpts with incomplete
  subdivision data are automatically excluded.

---

## Data (`data/`)

- `Mediciones_Microrritmos.xlsx`  
  Master dataset containing all microrhythmic measurements extracted from the MIDI
  corpus. Each row corresponds to a measured rhythmic event within a 16-beat excerpt.

- `corpus.md`  
  List of analyzed musical excerpts, organized by genre.

- `midi/`  
  Manually encoded MIDI files, organized by genre. Each file represents a perceptually
  grounded rhythmic reduction of a recorded performance.

---

## Figures (`figures/`)

This directory contains **curated figures** generated from the analysis scripts.
These figures correspond to results discussed in the written thesis and are intended
for inspection rather than bulk regeneration.

---

## Technologies

- Python  
- MIDI parsing libraries  
- NumPy  
- Pandas  
- Matplotlib  

All dependencies are listed in `requirements.txt`.

---

## Scope and limitations

- This project analyzes **symbolic timing only**; timbral, dynamic, and articulation
  features are outside its scope.
- The corpus is **small and curated by design**, prioritizing perceptual validity over
  statistical generalization.
- Higher-level metric ambiguity and expressive timing at larger temporal scales are
  not modeled.

---

## Status

This repository represents the **final research state** of the computational analysis
conducted for the undergraduate thesis. It is not intended as a continuously evolving
software project, but as a documented, inspectable research artifact suitable for
academic evaluation.
