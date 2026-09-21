from pathlib import Path

import pandas as pd


def analizar_datos(df: pd.DataFrame) -> dict:
    """Entrega un resumen básico del dataset."""
    resumen = {
        "filas": len(df),
        "columnas": list(df.columns),
        "categoria_mas_comun": df["categoria"].mode().iloc[0] if not df.empty else None,
        "precio_promedio": round(float(df["precio_promedio"].mean()), 2) if "precio_promedio" in df.columns else None,
        "distancia_promedio": round(float(df["distancia_km"].mean()), 2) if "distancia_km" in df.columns else None,
    }
    return resumen


if __name__ == "__main__":
    archivo = Path(__file__).resolve().parents[1] / "data" / "sitios_turisticos_cartago.csv"
    df = pd.read_csv(archivo)
    print(analizar_datos(df))
