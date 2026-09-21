from __future__ import annotations

import pandas as pd


def recomendar_sitios(df: pd.DataFrame, preferencia: str, presupuesto: float | int = 10000) -> pd.DataFrame:
    """Recomienda sitios según interés y presupuesto disponible."""
    textos = df["descripcion"].fillna("").str.lower()
    categoria = preferencia.lower()

    filtrado = df[
        (textos.str.contains(categoria, case=False, na=False)) |
        (df["categoria"].str.lower().str.contains(categoria, case=False, na=False))
    ].copy()

    if filtrado.empty:
        return df[df["precio_promedio"] <= presupuesto].head(3).copy()

    recomendados = filtrado[filtrado["precio_promedio"] <= presupuesto].copy()
    if recomendados.empty:
        recomendados = filtrado.head(3).copy()

    return recomendados.sort_values("precio_promedio").reset_index(drop=True)
