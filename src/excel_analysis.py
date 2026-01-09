import xlrd
import matplotlib.pyplot as plt

# ---------- CONFIGURACIÓN ----------
FILE_PATH = ""  # Ruta a Mediciones_Microrritmos.xlsx
GENERO = 1      # Cumbia=1, Salsa=2, Joesón=3, Bossa=4, Funk=5
CANCION = 1     # Índice de canción dentro del género (1-based)

# Subdivisiones por beat:
# 4 para todos los géneros
# 3 o 4 en el caso de funk brasileño, según el fragmento analizado
SUBDIVISIONS = 4  # Cambiar a 3 si el fragmento de funk lo requiere


# ---------- LECTURA DE EXCEL ----------
def read_durations(file_path, start_row, col, subdivisions):
    wb = xlrd.open_workbook(file_path)
    ws = wb.sheet_by_index(0)

    durations = []

    for j in range(col, col + subdivisions):
        try:
            value = ws.cell_value(start_row, j)
            if isinstance(value, (int, float)) and value > 10:
                durations.append(value)
            else:
                durations.append(None)
        except IndexError:
            durations.append(None)

    return durations


def get_title_name(file_path, col, row):
    wb = xlrd.open_workbook(file_path)
    ws = wb.sheet_by_index(0)
    try:
        return ws.cell_value(row, col)
    except IndexError:
        return "Sin nombre"


# ---------- CÁLCULO DE ÍNDICES ----------
BASE_COL = ((GENERO - 1) * 9) + 4
START_ROW = ((CANCION - 1) * 20) + 3
TITLE = get_title_name(FILE_PATH, BASE_COL - 4, START_ROW - 3)

# ---------- EXTRAER DATOS ----------
durations_per_beat = []
labels = []

for beat in range(16):
    row = START_ROW + beat
    values = read_durations(FILE_PATH, row, BASE_COL, SUBDIVISIONS)
    durations_per_beat.append(values)
    labels.append(f"T{beat + 1}")

# ---------- GRAFICAR ----------
plt.figure(figsize=(10, 6))

x = list(range(1, SUBDIVISIONS + 1))
colors = plt.cm.tab20.colors

for i, dur in enumerate(durations_per_beat):
    plt.plot(
        x,
        dur,
        marker="o",
        linestyle="-",
        color=colors[i % len(colors)],
        alpha=0.9,
        label=labels[i]
    )

plt.xlim(1, SUBDIVISIONS)
plt.xticks(x)
plt.ylim(12, 40)
plt.xlabel("Tipo de subdivisión")
plt.ylabel("Duración (%)")
plt.title(f"Duración de semicorcheas | {TITLE}")
plt.grid(True)
plt.legend(fontsize="x-small", ncol=2)
plt.tight_layout()
plt.show()
