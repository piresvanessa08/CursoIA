from pathlib import Path

import pandas as pd

from src.cargar_datos import cargar_datos
from src.eda_proyecto import analizar_datos
from src.recomendador import recomendar_sitios


def main() -> None:
    archivo = Path(__file__).resolve().parents[1] / "data" / "sitios_turisticos_cartago.csv"
    df = cargar_datos(archivo)

    print("Resumen del dataset:")
    print(analizar_datos(df))

    print("\nRecomendaciones para turismo histórico con presupuesto de 10000:")
    print(recomendar_sitios(df, preferencia="historia", presupuesto=10000))


if __name__ == "__main__":
    main()
