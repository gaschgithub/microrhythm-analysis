import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors

# ---------- CONFIGURACIÓN ----------
FILE_PATH = ""  # Ruta a Mediciones_Microrritmos.xlsx

# Selección y orden de géneros (mínimo 2, máximo 5)
# Opciones válidas: "Cumbia", "Salsa", "Joesón", "Bossa Nova", "Funk Brasileño"
SELECTED_GENRES = ["Funk Brasileño", "Bossa Nova", "Joesón", "Salsa", "Cumbia"]

SUBDIVISIONS = 4  # Este script compara solo 4 subdivisiones ("dieciseisavos")

Y_LIM = (20, 28)  # Ajusta si tu corpus produce otros rangos
TITLE = "Poligroove: Comparación de características microrrítmicas"

# Uniones entre géneros
CONNECT_GENRES = True


# ---------- MAPEO DE COLUMNAS (según layout del Excel) ----------
# BASE_COL = ((GENERO - 1) * 9) + 4
GENRE_IDS = {
    "Cumbia": 1,
    "Salsa": 2,
    "Joesón": 3,
    "Bossa Nova": 4,
    "Funk Brasileño": 5,
}

GENRE_COLORS = {
    "Cumbia": "darkviolet",
    "Salsa": "blue",
    "Joesón": "red",
    "Bossa Nova": "darkgoldenrod",
    "Funk Brasileño": "green",
}


# ---------- LECTURA DE EXCEL ----------
def read_genre_values(df: pd.DataFrame, genre: str) -> dict[str, list[float]]:
    genre_id = GENRE_IDS[genre]
    base_col = ((genre_id - 1) * 9) + 4
    cols = [base_col + i for i in range(SUBDIVISIONS)]

    block = df.iloc[:, cols].apply(pd.to_numeric, errors="coerce")

    # Caso especial: Funk Brasileño puede tener 3 subdivisiones detectadas.
    # Para la comparación entre géneros, usamos solo filas completas (4 valores).
    if genre == "Funk Brasileño":
        block = block.dropna(how="any")

    return {str(i + 1): block.iloc[:, i].dropna().tolist() for i in range(SUBDIVISIONS)}


def load_data(file_path: str, genres: list[str]) -> dict[str, dict[str, list[float]]]:
    df = pd.read_excel(file_path)
    return {g: read_genre_values(df, g) for g in genres}


# ---------- PROMEDIOS ----------
def mean_by_subdivision(data: dict[str, dict[str, list[float]]]) -> dict[str, list[float]]:
    means = {}
    for genre, vals in data.items():
        means[genre] = [
            (sum(vals[str(i)]) / len(vals[str(i)])) if vals[str(i)] else 0.0
            for i in range(1, SUBDIVISIONS + 1)
        ]
    return means


# ---------- GRÁFICA 3D ----------
def plot_3d_trends(means: dict[str, list[float]], genres: list[str]) -> None:
    fig = plt.figure(figsize=(14, 10))
    ax = fig.add_subplot(111, projection="3d")

    x_dense = np.linspace(1, SUBDIVISIONS, 120)

    for z, genre in enumerate(genres):
        y_points = means[genre]
        y_dense = np.interp(x_dense, [1, 2, 3, 4], y_points)
        z_dense = np.full_like(x_dense, z, dtype=float)

        ax.scatter(
            [1, 2, 3, 4],
            y_points,
            [z] * SUBDIVISIONS,
            s=50,
            color=GENRE_COLORS[genre],
            label=genre,
        )
        ax.plot(x_dense, y_dense, z_dense, color=GENRE_COLORS[genre], linewidth=2)

    if CONNECT_GENRES and len(genres) >= 2:
        for i in range(len(x_dense) - 1):
            for j in range(len(genres) - 1):
                xs = np.linspace(x_dense[i], x_dense[i + 1], 10)

                y_a0 = np.interp(x_dense[i], [1, 2, 3, 4], means[genres[j]])
                y_a1 = np.interp(x_dense[i + 1], [1, 2, 3, 4], means[genres[j]])
                y_b0 = np.interp(x_dense[i], [1, 2, 3, 4], means[genres[j + 1]])
                y_b1 = np.interp(x_dense[i + 1], [1, 2, 3, 4], means[genres[j + 1]])

                ys0 = np.linspace(y_a0, y_b0, 10)
                ys1 = np.linspace(y_a1, y_b1, 10)
                zs = np.linspace(j, j + 1, 10)

                c0 = np.array(colors.to_rgb(GENRE_COLORS[genres[j]]))
                c1 = np.array(colors.to_rgb(GENRE_COLORS[genres[j + 1]]))

                for k in range(9):
                    t = k / 9
                    line_color = c0 * (1 - t) + c1 * t
                    ax.plot(
                        [xs[k], xs[k + 1]],
                        [ys0[k], ys1[k + 1]],
                        [zs[k], zs[k + 1]],
                        color=line_color,
                        linewidth=1.2,
                        alpha=0.9,
                    )

    ax.set_xlabel("Tipo de dieciseisavo")
    ax.set_xlim(1, SUBDIVISIONS)
    ax.set_xticks([1, 2, 3, 4])

    ax.set_ylabel("Duración promedio (%)")
    ax.set_ylim(*Y_LIM)

    ax.set_zlabel("Género")
    ax.set_zticks(range(len(genres)))
    ax.set_zticklabels(genres)

    plt.title(TITLE)
    plt.legend()
    plt.tight_layout()
    plt.show()


# ---------- EJECUCIÓN ----------
if __name__ == "__main__":
    if not FILE_PATH:
        raise ValueError("Define FILE_PATH con la ruta a Mediciones_Microrritmos.xlsx")

    unknown = [g for g in SELECTED_GENRES if g not in GENRE_IDS]
    if unknown:
        raise ValueError(f"Géneros inválidos en SELECTED_GENRES: {unknown}")

    if len(SELECTED_GENRES) < 2 or len(SELECTED_GENRES) > 5:
        raise ValueError("SELECTED_GENRES debe contener de 2 a 5 géneros")

    data = load_data(FILE_PATH, SELECTED_GENRES)
    means = mean_by_subdivision(data)
    plot_3d_trends(means, SELECTED_GENRES)
