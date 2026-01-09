import xlrd
import matplotlib.pyplot as plt
from collections import defaultdict
from math import sqrt

# ---------- CONFIGURACIÓN ----------
FILE_PATH = ""   # Ruta a Mediciones_Microrritmos.xlsx
GENERO = 1       # Cumbia=1, Salsa=2, Joesón=3, Bossa=4, Funk=5

# Subdivisiones por beat:
# 4 para todos los géneros
# 3 o 4 en el caso de funk brasileño, según el fragmento analizado
SUBDIVISIONS = 4  # Cambiar a 3 si el fragmento de funk lo requiere

MIN_ROWS = 3
MAX_ROWS = 499


# ---------- LECTURA DE EXCEL ----------
def read_durations(file_path, min_rows, max_rows, col):
    wb = xlrd.open_workbook(file_path)
    ws = wb.sheet_by_index(0)

    durations = []

    for i in range(min_rows, max_rows):
        for j in range(col, col + SUBDIVISIONS):
            try:
                value = ws.cell_value(i, j)
                if isinstance(value, (int, float)) and value > 10:
                    durations.append(value)
            except IndexError:
                pass

    return durations


# ---------- ANÁLISIS ESTADÍSTICO ----------
def analyze_durations(durations, mean_value):
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
            ((value - mean_value) ** 2) * (counts[value] / len(durations))
        )
        y_values.append(value)
        indicators.append(counts[value])

    std_dev = sqrt(sum(variance_terms))
    return y_values, indicators, std_dev


# ---------- SELECCIÓN DE COLUMNAS ----------
BASE_COL = ((GENERO - 1) * 9) + 4

durations_per_subdivision = [
    read_durations(FILE_PATH, MIN_ROWS, MAX_ROWS, BASE_COL + i)
    for i in range(SUBDIVISIONS)
]

mean_durations = [
    round(sum(d) / len(d), 3) if d else 0
    for d in durations_per_subdivision
]

results = [
    analyze_durations(dur, mean)
    for dur, mean in zip(durations_per_subdivision, mean_durations)
]


# ---------- PREPARAR DATOS PARA GRÁFICA ----------
x_values = []
y_values = []
sizes = []

for idx, (y, indicators, _) in enumerate(results, start=1):
    x_values.extend([idx] * len(y))
    y_values.extend(y)
    sizes.extend(indicators)


# ---------- IMPRIMIR ESTADÍSTICAS ----------
for idx, (_, _, std) in enumerate(results, start=1):
    print(f"Promedio duración {idx}: {mean_durations[idx - 1]}")
    print(f"Desviación estándar {idx}: {std}")


# ---------- GRÁFICA ----------
plt.figure(figsize=(10, 6))
plt.scatter(
    x_values,
    y_values,
    s=[s * 10 for s in sizes],
    alpha=0.5
)

plt.xlim(1, SUBDIVISIONS)
plt.xticks(range(1, SUBDIVISIONS + 1))
plt.ylim(16, 34)
plt.xlabel("Tipo de subdivisión")
plt.ylabel("Duración (%)")

GENRES = ["CUMBIA", "SALSA", "JOESÓN", "BOSSA NOVA", "FUNK BRASILEÑO"]
plt.title(f"Duración de subdivisiones | {GENRES[GENERO - 1]}")
plt.grid(True)

# Promedios
plt.plot(
    range(1, SUBDIVISIONS + 1),
    mean_durations,
    marker="o",
    label="Duración promedio"
)

plt.legend()
plt.tight_layout()
plt.show()

