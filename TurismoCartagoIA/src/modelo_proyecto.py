"""Entrena, evalúa y guarda modelos de clasificación para TurismoCartagoIA."""

from __future__ import annotations

from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier

try:
    from .perceptron_proyecto import entrenar_perceptron, sigmoid
except ImportError:
    from perceptron_proyecto import entrenar_perceptron, sigmoid


PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_DIR / "data" / "sitios_turisticos_cartago.csv"
MODEL_PATH = PROJECT_DIR / "models" / "modelo_turismo.joblib"
CHART_PATH = PROJECT_DIR / "graficos" / "matriz_confusion_modelo.png"
METRICS_PATH = PROJECT_DIR / "data" / "comparacion_modelos.csv"
FEATURES = ["categoria", "calificacion", "es_gratuito"]
NUMERIC_FEATURES = ["calificacion", "es_gratuito"]


def construir_pipeline(clasificador) -> Pipeline:
    preprocesamiento = ColumnTransformer(
        transformers=[
            ("numericas", StandardScaler(), NUMERIC_FEATURES),
            ("categoria", OneHotEncoder(handle_unknown="ignore"), ["categoria"]),
        ]
    )
    return Pipeline(
        [("preprocesamiento", preprocesamiento), ("modelo", clasificador)]
    )


def preparar_dataset() -> tuple[pd.DataFrame, pd.Series, float]:
    datos = pd.read_csv(DATA_PATH)
    columnas_fuente = {"categoria", "visitantes_mes", "calificacion", "precio"}
    faltantes = columnas_fuente.difference(datos.columns)
    if faltantes:
        raise ValueError(f"Faltan columnas para entrenar: {', '.join(sorted(faltantes))}")

    datos["visitantes_mes"] = pd.to_numeric(datos["visitantes_mes"], errors="coerce")
    datos["calificacion"] = pd.to_numeric(datos["calificacion"], errors="coerce")
    datos["precio"] = pd.to_numeric(datos["precio"], errors="coerce")
    # Replica la característica derivada de preparacion_datos.py sin imputar vacíos.
    datos["es_gratuito"] = datos["precio"].map(
        lambda precio: np.nan if pd.isna(precio) else int(precio == 0)
    )
    entrenables = datos.dropna(
        subset=["categoria", "visitantes_mes", "calificacion", "precio", "es_gratuito"]
    ).copy()
    if len(entrenables) < 6:
        raise ValueError(
            "Se requieren al menos seis sitios con visitantes, calificación y precio "
            "documentados para crear una división de entrenamiento/prueba."
        )

    umbral = float(entrenables["visitantes_mes"].median())
    y = (entrenables["visitantes_mes"] >= umbral).astype(int).rename("alta_afluencia")
    X = entrenables[FEATURES].copy()
    if y.value_counts().min() < 2:
        raise ValueError("Se necesitan al menos dos ejemplos de cada clase.")
    print(
        f"Registros utilizables: {len(entrenables)} de {len(datos)}. "
        f"Se excluyeron {len(datos) - len(entrenables)} sitios con datos incompletos."
    )
    if "datos_estimados" in entrenables:
        estimados = int(
            pd.to_numeric(entrenables["datos_estimados"], errors="coerce")
            .fillna(0)
            .eq(1)
            .sum()
        )
        prorrateados = (
            int(entrenables["participacion_hipotetica_pct"].notna().sum())
            if "participacion_hipotetica_pct" in entrenables
            else 0
        )
        if estimados or prorrateados:
            print(
                f"Advertencia: {estimados} registros contienen aproximaciones y "
                f"{prorrateados} visitantes provienen de prorrateo hipotético; "
                "las métricas son solo demostrativas."
            )
    print(f"Objetivo: alta afluencia = visitantes_mes >= mediana ({umbral:.0f}).")
    return X, y, umbral


def entrenar_y_evaluar() -> dict:
    X, y, umbral = preparar_dataset()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"Sitios para entrenar: {len(X_train)} | sitios para probar: {len(X_test)}")

    clases_minoritarias = int(y_train.value_counts().min())
    n_splits = min(5, clases_minoritarias)
    if n_splits < 2:
        raise ValueError("No hay suficientes casos por clase para validación cruzada.")
    cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
    modelos = {
        "Regresión logística": construir_pipeline(
            LogisticRegression(max_iter=1000, class_weight="balanced")
        ),
        # Un vecino permite ajustar la validación cruzada aun con este dataset pequeño.
        "KNN (1 vecino)": construir_pipeline(KNeighborsClassifier(n_neighbors=1)),
        "Árbol de decisión": construir_pipeline(
            DecisionTreeClassifier(max_depth=3, class_weight="balanced", random_state=42)
        ),
    }

    resultados = []
    modelos_entrenados = {}
    for nombre, pipeline in modelos.items():
        f1_cv = cross_val_score(pipeline, X_train, y_train, cv=cv, scoring="f1")
        pipeline.fit(X_train, y_train)
        predicciones = pipeline.predict(X_test)
        resultados.append(
            {
                "Modelo": nombre,
                "Exactitud": accuracy_score(y_test, predicciones),
                "Precisión": precision_score(y_test, predicciones, zero_division=0),
                "Recall": recall_score(y_test, predicciones, zero_division=0),
                "F1 prueba": f1_score(y_test, predicciones, zero_division=0),
                "F1 validación cruzada promedio": float(f1_cv.mean()),
                "F1 validación cruzada desviación": float(f1_cv.std()),
            }
        )
        modelos_entrenados[nombre] = pipeline

    tabla = pd.DataFrame(resultados).sort_values(
        "F1 validación cruzada promedio", ascending=False
    )
    tabla.to_csv(METRICS_PATH, index=False)
    print("\nComparación de modelos (la selección usa F1 de validación cruzada):")
    print(tabla.round(3).to_string(index=False))
    mejor_nombre = str(tabla.iloc[0]["Modelo"])
    mejor_modelo = modelos_entrenados[mejor_nombre]
    print(f"\nMejor modelo según F1 de validación cruzada: {mejor_nombre}")

    predicciones_test = mejor_modelo.predict(X_test)
    matriz = confusion_matrix(y_test, predicciones_test, labels=[0, 1])
    CHART_PATH.parent.mkdir(parents=True, exist_ok=True)
    figura, eje = plt.subplots(figsize=(6, 5))
    sns.heatmap(
        matriz,
        annot=True,
        fmt="d",
        cmap="Blues",
        cbar=False,
        xticklabels=["Predijo baja", "Predijo alta"],
        yticklabels=["Real baja", "Real alta"],
        ax=eje,
    )
    eje.set_title(f"Matriz de confusión — {mejor_nombre}")
    eje.set_xlabel("Predicción")
    eje.set_ylabel("Clase real")
    figura.tight_layout()
    figura.savefig(CHART_PATH, dpi=150)
    plt.close(figura)

    manual = comparar_perceptron(X_train, X_test, y_train, y_test)
    print(
        "\nPerceptrón NumPy desde cero (mismo conjunto de prueba, solo calificación "
        f"y acceso gratuito): F1={manual['F1']:.3f}, exactitud={manual['Exactitud']:.3f}"
    )
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(
        {
            "modelo": mejor_modelo,
            "nombre_modelo": mejor_nombre,
            "umbral_visitantes": umbral,
            "columnas_entrada": FEATURES,
            "clase_positiva": f"visitantes_mes >= {umbral:.0f}",
        },
        MODEL_PATH,
    )
    print(f"Matriz de confusión: {CHART_PATH}")
    print(f"Métricas: {METRICS_PATH}")
    print(f"Modelo guardado: {MODEL_PATH}")
    print(
        "Advertencia: el conjunto utilizable es pequeño; las métricas son inestables "
        "y no representan una predicción turística validada en población."
    )
    return {"tabla": tabla, "mejor_modelo": mejor_nombre, "umbral": umbral}


def comparar_perceptron(X_train, X_test, y_train, y_test) -> dict[str, float]:
    """Evalúa la implementación NumPy existente con el mismo holdout."""
    columnas = ["calificacion", "es_gratuito"]
    escalador = StandardScaler().fit(X_train[columnas])
    entradas_train = escalador.transform(X_train[columnas])
    entradas_test = escalador.transform(X_test[columnas])
    perceptron = entrenar_perceptron(entradas_train, y_train.to_numpy(dtype=float))
    probabilidades = sigmoid(entradas_test @ perceptron.weights + perceptron.bias)
    predicciones = (probabilidades >= 0.5).astype(int)
    return {
        "Exactitud": float(accuracy_score(y_test, predicciones)),
        "F1": float(f1_score(y_test, predicciones, zero_division=0)),
    }


if __name__ == "__main__":
    entrenar_y_evaluar()
