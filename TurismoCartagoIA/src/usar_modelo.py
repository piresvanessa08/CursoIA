"""Carga el Pipeline guardado y estima si escenarios nuevos tendrían alta afluencia."""

from pathlib import Path

import joblib
import pandas as pd


PROJECT_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = PROJECT_DIR / "models" / "modelo_turismo.joblib"


def predecir_escenarios() -> pd.DataFrame:
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            f"No existe {MODEL_PATH}. Ejecuta primero: python src/modelo_proyecto.py"
        )
    artefacto = joblib.load(MODEL_PATH)
    modelo = artefacto["modelo"]
    escenarios = pd.DataFrame(
        [
            {"caso": "Religioso, hipotético A", "categoria": "Religioso", "calificacion": 4.5, "es_gratuito": 1},
            {"caso": "Cultural, hipotético B", "categoria": "Cultural", "calificacion": 4.2, "es_gratuito": 0},
            {"caso": "Recreativo, hipotético C", "categoria": "Recreativo", "calificacion": 4.7, "es_gratuito": 1},
        ]
    )
    X_nuevos = escenarios[artefacto["columnas_entrada"]]
    probabilidades = modelo.predict_proba(X_nuevos)[:, list(modelo.classes_).index(1)]
    predicciones = modelo.predict(X_nuevos)
    escenarios["probabilidad_alta_afluencia_%"] = (probabilidades * 100).round(1)
    escenarios["prediccion"] = [
        "Alta afluencia" if valor == 1 else "Afluencia menor a la mediana"
        for valor in predicciones
    ]
    escenarios["umbral_visitantes_usado"] = artefacto["umbral_visitantes"]
    print(f"Modelo cargado: {artefacto['nombre_modelo']}")
    print(
        "Los tres registros de demostración son escenarios hipotéticos; sus "
        "calificaciones y precios no describen sitios reales."
    )
    print(escenarios.to_string(index=False))
    return escenarios


if __name__ == "__main__":
    predecir_escenarios()
