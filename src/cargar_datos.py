from pathlib import Path
import pandas as pd


def cargar_datos(ruta_csv: str | Path) -> pd.DataFrame:
    """Carga el archivo CSV de sitios turísticos."""
    ruta = Path(ruta_csv)
    if not ruta.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {ruta}")

    df = pd.read_csv(ruta)
    return df


if __name__ == "__main__":
    archivo = Path(__file__).resolve().parents[1] / "data" / "sitios_turisticos_cartago.csv"
    datos = cargar_datos(archivo)
    print(datos.head())
