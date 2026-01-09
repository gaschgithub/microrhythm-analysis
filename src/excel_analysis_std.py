"""
Excel-based microrhythm analysis (mean and standard deviation).

This module analyzes sixteenth-note duration data exported to Excel,
computes mean values and standard deviation, and generates scatter plots
to visualize microrhythmic tendencies across musical genres.
"""

import xlrd
import matplotlib.pyplot as plt
from collections import defaultdict
from math import sqrt


def read_durations_from_excel(file_path, min_rows, max_rows, start_col):
    """
    Read sixteenth-note durations from an Excel file.
    """
    workbook = xlrd.open_workbook(file_path)
    sheet = workbook.sheet_by_index(0)

    durations = []

    for i in range(min_rows, max_rows):
        try:
            value = sheet.cell_value(i, start_col)
            if isinstance(value, (int, float)) and value > 10:
                durations.append(value)
        except ValueError:
            pass

    return durations


def analyze_durations(durations, mean_duration):
    """
    Compute frequency-weighted standard deviation of duration values.
    """
    unique_values = {}
    counts = defaultdict(int)

    for value in durations:
        rounded = round(value, 5)
        if rounded not in unique_values.values():
            key = f"x{len(unique_values) + 1}"
            unique_values[key] = rounded
        counts[rounded] += 1

    variance_terms = []
    y_values = []
    indicators = []

    for value in unique_values.values():
        variance_terms.append(
            ((value - mean_duration) ** 2) * (counts[value] / len(durations))
        )
        y_values.append(float(value))
        indicators.append(int(counts[value]))

    std_dev = sqrt(sum(variance_terms))
    return y_values, indicators, std_dev


def plot_microrhythm_scatter(y_values, sizes, mean_values, genre, subdivisions):
    """
    Generate scatter plot of microrhythmic duration distributions.
    """
    x_vals = []
    y_vals = []
    size_vals = []

    for idx, (y, s) in enumerate(zip(y_values, sizes), start=1):
        x_vals.extend([idx] * len(y))
        y_vals.extend(y)
        size_vals.extend(s)

    plt.figure(figsize=(10, 6))
    plt.scatter(
        x_vals,
        y_vals,
        s=[size * 10 for size in size_vals],
        alpha=0.5
    )

    plt.xlim(1, subdivisions)
    plt.xticks(range(1, subdivisions + 1))
    plt.xlabel("Sixteenth-note type")
    plt.ylabel("Duration (%)")
    plt.title(f"Microrhythmic durations — {genre}")
    plt.grid(True)

    plt.plot(
        list(range(1, subdivisions + 1)),
        mean_values,
        marker="o",
        label="Mean duration"
    )

    plt.legend()
    plt.show()
