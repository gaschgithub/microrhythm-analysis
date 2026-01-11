# Microrhythm Analysis

This repository contains the data, analysis scripts, and figures developed for my
undergraduate thesis in Music and Artistic Technology (UNAM):

**_Microrhythms in Latin Popular Music: Quantification and Synthesis of Latin Sabor_**

The project investigates **systematic microrhythmic timing deviations** in selected
Latin popular music genres using **symbolic representations (MIDI)** derived from
perceptually identified rhythmic events. Timing deviations are quantified through
inter-onset interval (IOI) analysis and expressed as percentages relative to a nominal
beat duration at a fixed tempo.

The computational findings informed the composition and production
of an original music album released under my artistic project **Gasch**.

This repository is conceived as a **research system**, prioritizing methodological
clarity and reproducibility over automation or large-scale processing.

---

## Thesis and artistic outcome

- 📄 **Undergraduate thesis (TESIUNAM repository):**  
  https://ru.dgb.unam.mx/items/1fdea9ae-5813-4caf-b2e7-4161eaeaec6e

- 🎧 **Resulting album (Gasch – _Hyperestesia_):**  
  https://orcd.co/hyperstesiagasch

The analytical work documented here informed the rhythmic design strategies
used in the album, which explores stylistic “sabor” through the synthesis of rhythmic prototypes from the studied genres. This flow between **analysis and creation** situates the project within a practice-based research paradigm, where computational tools support artistic inquiry.

---

## Research motivation and hypothesis

This research originates from an **artistic motivation**: as a musician, I sought to
compose music inspired by Latin popular genres **without relying on extensive prior knowledge**, instead grounding compositional decisions in
measured rhythmic behavior.

The central hypothesis of the investigation is:

> The “sabor” of the musical genres salsa, cumbia, joesón, bossa nova, and
> Brazilian funk can be synthesized into **repeating rhythmic pattern prototypes**
> encoding genre-specific characteristics in **accentuation, articulation, and
> microtiming of sixteenth notes**, within a tempo range (BPM) derived from the studied
> corpus.

Here, microrhythm is presented not as expressive deviation or error,
but as a **structural carrier of stylistic information** that can be analyzed,
formalized, and re-applied in creative contexts.

---

## Research focus

The project addresses the following research questions:

- How are microrhythmic timing deviations distributed at the subdivision level within
  Latin popular music genres?
- Do these deviations form **stable, genre-specific profiles** across multiple musical
  excerpts?
- Can symbolic microrhythmic measurements support the construction of **rhythmic
  prototypes** per genre?

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
  
A complete list of analyzed excerpts is provided in `data/corpus.md`.

All rhythmic events were **identified perceptually** and encoded manually prior to
analysis. No automatic onset detection was used.

> **Note:** While the written thesis discusses a broader stylistic context, this
> repository contains the finalized microrhythmic dataset (MIDI templates) used for quantitative
> analysis and figure generation.

---

## Method overview

The analysis pipeline implemented in this repository follows these steps:

1. **Perceptual identification** of salient rhythmic events in recorded performances.
2. **Manual encoding** of these events as MIDI sequences (16-beat excerpts).
3. **Extraction of onset times** from MIDI files.
4. **Computation of inter-onset intervals (IOIs)** in milliseconds.
5. **Inference of beat subdivisions** from onset distributions.
6. **Normalization of timing deviations** relative to the nominal beat duration.
7. **Statistical analysis and visualization** at the subdivision level.

Symbolic representations are used deliberately to allow for precise timing analysis and
explicit control over rhythmic structure, at the cost of excluding timbral and
micro-dynamic dimensions.

---

### Subdivision modeling

Most analyzed genres exhibit a consistent **four-part subdivision of the beat**
(corresponding to sixteenth notes). However, Brazilian funk excerpts may alternate
between **three- and four-part subdivisions**, sometimes within the same musical
fragment.

This variability is handled as follows:

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
  their shared derivation from son-based rhythms.
- **Cumbia** appears closer to Salsa/Joesón than to Brazilian genres, reflecting Caribbean rhythmic influence and shared approaches to off-beat timing.
- **Bossa Nova and Brazilian Funk** form a more distant group relative to the above,
  showing tendencies associated with samba-derived practices and, in the case of funk,
  subdivision alternation.

These results support the hypothesis that microrhythmic duration patterns can reflect
tacit stylistic consensus across genres and can be formalized into rhythmic prototypes.

---

## Repository structure

```
microrhythm-analysis/
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
  Results are exported to Excel for later analysis.

- `excel_analysis_std.py`  
  Statistical analysis of microrhythmic duration data exported to Excel. Computes mean
  values and frequency-weighted standard deviation, and generates scatter plots to
  visualize duration distributions at the subdivision level.

- `excel_analysis.py`  
  Visualization of microrhythmic timing for individual musical excerpts across 16
  analyzed beats of a single song.

- `excel_genre_comparison.py`  
  Cross-genre comparison of average sixteenth-note (four-subdivision) durations.
  Generates a three-dimensional visualization to compare
  microrhythmic profiles across genres.

---

## Scope and limitations

- This project analyzes **symbolic timing only**; timbral, dynamic, and articulation
  features are outside its scope.
- The corpus is **small and curated by design**, prioritizing perceptual validity over
  statistical generalization.
- Higher-level metric ambiguity and long-range expressive timing are not modeled.

---

## Status

This repository represents the **final research state** of the computational analysis
conducted for the undergraduate thesis. It is not intended as a continuously evolving
software project, but as a documented research artifact.
