"""Perceptrón logístico didáctico para el avance 2 de TurismoCartago IA."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if __package__:
    from .preparacion_datos import (
        agregar_caracteristicas,
        cargar_datos,
        limpiar_datos,
    )
else:
    from preparacion_datos import agregar_caracteristicas, cargar_datos, limpiar_datos


PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_DIR / "data" / "sitios_turisticos_cartago.csv"
FEATURE_COLUMNS = ("calificacion", "es_gratuito")
LEARNING_RATE = 0.1
EPOCHS = 2_000


@dataclass
class PerceptronResult:
    weights: np.ndarray
    bias: float
    loss_history: list[float]


def sigmoid(logits: np.ndarray) -> np.ndarray:
    """Calcula sigmoide con límites para evitar desbordamiento numérico."""
    logits = np.clip(logits, -500, 500)
    return 1 / (1 + np.exp(-logits))


def binary_cross_entropy(y_true: np.ndarray, probabilities: np.ndarray) -> float:
    probabilities = np.clip(probabilities, 1e-12, 1 - 1e-12)
    return float(
        -np.mean(
            y_true * np.log(probabilities)
            + (1 - y_true) * np.log(1 - probabilities)
        )
    )


def preparar_datos(
    datos: pd.DataFrame,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, float]:
    """Crea entradas escaladas y objetivo binario sin incluir el objetivo en X."""
    columnas_requeridas = {"visitantes_mes", *FEATURE_COLUMNS}
    faltantes = columnas_requeridas.difference(datos.columns)
    if faltantes:
        raise ValueError(
            "Faltan columnas requeridas para el perceptrón: "
            + ", ".join(sorted(faltantes))
        )
    if datos.empty:
        raise ValueError("No hay registros para entrenar el perceptrón.")

    visitantes = datos["visitantes_mes"].to_numpy(dtype=float)
    umbral = float(np.median(visitantes))
    y = (visitantes >= umbral).astype(float)
    X_original = datos.loc[:, FEATURE_COLUMNS].to_numpy(dtype=float)

    medias = X_original.mean(axis=0)
    desviaciones = X_original.std(axis=0)
    if np.any(desviaciones == 0):
        constantes = [
            FEATURE_COLUMNS[i]
            for i in np.flatnonzero(desviaciones == 0)
        ]
        raise ValueError(
            "No se pueden estandarizar columnas constantes: "
            + ", ".join(constantes)
        )

    X_escalado = (X_original - medias) / desviaciones
    return X_escalado, y, medias, desviaciones, umbral


def entrenar_perceptron(
    X: np.ndarray,
    y: np.ndarray,
    learning_rate: float = LEARNING_RATE,
    epochs: int = EPOCHS,
) -> PerceptronResult:
    if X.ndim != 2 or X.shape[1] != 2:
        raise ValueError("El perceptrón requiere exactamente dos variables de entrada.")
    if y.ndim != 1 or len(y) != len(X) or len(y) == 0:
        raise ValueError("X e y deben tener el mismo número de filas no vacío.")
    if not np.isin(y, (0, 1)).all():
        raise ValueError("La variable objetivo solo puede contener valores 0 y 1.")
    if learning_rate <= 0 or epochs <= 0:
        raise ValueError("La tasa de aprendizaje y las épocas deben ser positivas.")

    weights = np.zeros(X.shape[1], dtype=float)
    bias = 0.0
    loss_history: list[float] = []

    for _ in range(epochs):
        probabilities = sigmoid(X @ weights + bias)
        loss_history.append(binary_cross_entropy(y, probabilities))

        error = probabilities - y
        weights -= learning_rate * (X.T @ error) / len(y)
        bias -= learning_rate * float(error.mean())

    final_probabilities = sigmoid(X @ weights + bias)
    loss_history.append(binary_cross_entropy(y, final_probabilities))
    return PerceptronResult(weights, bias, loss_history)


def cargar_dataset() -> tuple[pd.DataFrame, float]:
    datos = limpiar_datos(cargar_datos(DATA_PATH))
    datos = agregar_caracteristicas(datos)
    return datos, float(np.median(datos["visitantes_mes"].to_numpy(dtype=float)))


def guardar_curva_aprendizaje(
    loss_history: list[float], output_dir: Path
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    ruta = output_dir / "perceptron_curva_aprendizaje.png"
    figura, eje = plt.subplots(figsize=(8, 5))
    eje.plot(loss_history, color="#2563eb", linewidth=2)
    eje.set_title("Curva de aprendizaje del perceptrón")
    eje.set_xlabel("Época")
    eje.set_ylabel("Pérdida logarítmica (binary cross-entropy)")
    eje.grid(True, alpha=0.3)
    figura.tight_layout()
    figura.savefig(ruta, dpi=150)
    plt.close(figura)
    return ruta


def guardar_frontera_decision(
    X: np.ndarray,
    y: np.ndarray,
    result: PerceptronResult,
    output_dir: Path,
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    ruta = output_dir / "perceptron_frontera_decision.png"
    figura, eje = plt.subplots(figsize=(8, 5))

    for clase, etiqueta, color, marcador in (
        (0, "Afluencia menor a la mediana", "#2563eb", "o"),
        (1, "Afluencia igual o mayor a la mediana", "#dc2626", "^"),
    ):
        mascara = y == clase
        eje.scatter(
            X[mascara, 0],
            X[mascara, 1],
            label=etiqueta,
            color=color,
            marker=marcador,
            s=85,
            edgecolor="black",
            zorder=3,
        )

    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    if abs(result.weights[1]) > 1e-12:
        x_line = np.linspace(x_min, x_max, 200)
        y_line = -(result.weights[0] * x_line + result.bias) / result.weights[1]
        eje.plot(x_line, y_line, color="black", linestyle="--", label="Frontera (p = 0,5)")
    elif abs(result.weights[0]) > 1e-12:
        eje.axvline(
            -result.bias / result.weights[0],
            color="black",
            linestyle="--",
            label="Frontera (p = 0,5)",
        )

    eje.set_xlim(x_min, x_max)
    eje.set_ylim(y_min, y_max)
    eje.set_title("Frontera de decisión del perceptrón")
    eje.set_xlabel("Calificación estandarizada")
    eje.set_ylabel("Acceso gratuito estandarizado")
    eje.legend(fontsize=8)
    eje.grid(True, alpha=0.3)
    figura.tight_layout()
    figura.savefig(ruta, dpi=150)
    plt.close(figura)
    return ruta


def ejecutar(output_dir: Path = PROJECT_DIR / "graficos") -> PerceptronResult:
    datos, _ = cargar_dataset()
    X, y, medias, desviaciones, umbral = preparar_datos(datos)
    result = entrenar_perceptron(X, y)

    predicciones = (sigmoid(X @ result.weights + result.bias) >= 0.5).astype(int)
    exactitud = float(np.mean(predicciones == y))
    perdida_inicial = result.loss_history[0]
    perdida_final = result.loss_history[-1]

    curva = guardar_curva_aprendizaje(result.loss_history, output_dir)
    frontera = guardar_frontera_decision(X, y, result, output_dir)

    print("PERCEPTRÓN DESDE CERO — DEMOSTRACIÓN ACADÉMICA")
    print(f"Registros: {len(datos)}")
    print(f"Objetivo: visitantes_mes >= mediana ({umbral:.0f})")
    print("Entradas: calificacion y es_gratuito, estandarizadas")
    print(f"Medias usadas para escalar: {medias}")
    print(f"Desviaciones estándar usadas: {desviaciones}")
    print(f"w1 (calificación): {result.weights[0]:.6f}")
    print(f"w2 (acceso gratuito): {result.weights[1]:.6f}")
    print(f"b: {result.bias:.6f}")
    print(f"Pérdida inicial: {perdida_inicial:.6f}")
    print(f"Pérdida final: {perdida_final:.6f}")
    print(f"Exactitud sobre estos mismos {len(datos)} registros: {exactitud:.2%}")
    print(f"Curva de aprendizaje: {curva}")
    print(f"Frontera de decisión: {frontera}")
    print(
        "Limitación: la exactitud es de entrenamiento, no una validación "
        "independiente. Siete registros no permiten afirmar generalización."
    )
    return result


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Entrena un perceptrón didáctico con los datos turísticos."
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=PROJECT_DIR / "graficos",
        help="Carpeta donde se guardan los dos gráficos.",
    )
    args = parser.parse_args()
    ejecutar(args.output_dir)


if __name__ == "__main__":
    main()
