from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler


PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_DIR / "data" / "sitios_turisticos_cartago.csv"

REQUIRED_COLUMNS = {
    "nombre",
    "categoria",
    "visitantes_mes",
    "calificacion",
    "precio",
    "horario",
}
NUMERIC_COLUMNS = ["visitantes_mes", "calificacion", "precio"]


def cargar_datos(archivo_csv):
    datos = pd.read_csv(archivo_csv)
    columnas_faltantes = REQUIRED_COLUMNS.difference(datos.columns)
    if columnas_faltantes:
        raise ValueError(
            "Faltan columnas requeridas en el CSV: "
            + ", ".join(sorted(columnas_faltantes))
        )
    return datos


def explorar_datos(datos):
    print(f"Dimensiones: {datos.shape[0]} filas, {datos.shape[1]} columnas")
    print("\nPrimeras filas:")
    print(datos.head())
    print("\nTipos de datos:")
    print(datos.dtypes)
    print("\nEstadísticas descriptivas:")
    print(datos.describe(include="all"))
    print("\nValores nulos por columna:")
    print(datos.isnull().sum())
    print(f"\nFilas duplicadas: {datos.duplicated().sum()}")


def limpiar_datos(datos):
    datos_limpios = datos.drop_duplicates().copy()

    for columna in datos_limpios.columns:
        if not datos_limpios[columna].isnull().any():
            continue

        if pd.api.types.is_numeric_dtype(datos_limpios[columna]):
            valor_relleno = datos_limpios[columna].median()
        else:
            valores = datos_limpios[columna].mode()
            if valores.empty:
                raise ValueError(
                    f"No se puede imputar '{columna}': no hay valores disponibles."
                )
            valor_relleno = valores.iloc[0]

        if pd.isna(valor_relleno):
            raise ValueError(
                f"No se puede imputar '{columna}': todos sus valores están vacíos."
            )
        datos_limpios[columna] = datos_limpios[columna].fillna(valor_relleno)
        print(f"Valores faltantes de '{columna}' imputados con: {valor_relleno}")

    duplicados_eliminados = len(datos) - len(datos_limpios)
    if duplicados_eliminados:
        print(f"Filas duplicadas eliminadas: {duplicados_eliminados}")
    else:
        print("No se encontraron filas duplicadas.")

    return datos_limpios


def visualizar_datos(datos, output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    sns.set_theme(style="whitegrid")

    figura, eje = plt.subplots(figsize=(9, 5))
    sns.barplot(
        data=datos,
        x="categoria",
        y="visitantes_mes",
        errorbar=None,
        ax=eje,
    )
    eje.set_title("Visitantes mensuales promedio por categoría")
    eje.set_xlabel("Categoría")
    eje.set_ylabel("Visitantes mensuales promedio")
    eje.tick_params(axis="x", rotation=30)
    figura.tight_layout()
    figura.savefig(output_dir / "seaborn_visitantes_categoria.png", dpi=150)
    plt.close(figura)

    figura, eje = plt.subplots(figsize=(9, 5))
    sns.scatterplot(
        data=datos,
        x="visitantes_mes",
        y="calificacion",
        hue="categoria",
        s=100,
        ax=eje,
    )
    eje.set_title("Visitantes mensuales y calificación por sitio")
    eje.set_xlabel("Visitantes mensuales")
    eje.set_ylabel("Calificación")
    figura.tight_layout()
    figura.savefig(output_dir / "seaborn_visitantes_calificacion.png", dpi=150)
    plt.close(figura)

    print(f"\nGráficos de Seaborn guardados en: {output_dir}")


def preparar_ml(datos):
    datos_ml = datos[["categoria", *NUMERIC_COLUMNS]].copy()
    datos_ml = pd.get_dummies(
        datos_ml,
        columns=["categoria"],
        prefix="categoria",
        dtype=int,
    )

    escalador = StandardScaler()
    datos_ml[NUMERIC_COLUMNS] = escalador.fit_transform(datos_ml[NUMERIC_COLUMNS])
    return datos_ml


def main():
    datos = cargar_datos(DATA_PATH)
    explorar_datos(datos)

    datos_limpios = limpiar_datos(datos)
    visualizar_datos(datos_limpios, PROJECT_DIR / "graficos")

    datos_ml = preparar_ml(datos_limpios)
    ruta_salida = PROJECT_DIR / "data" / "sitios_turisticos_preparados_ml.csv"
    datos_ml.to_csv(ruta_salida, index=False)
    print(f"\nDatos preparados para exploración de ML guardados en: {ruta_salida}")
    print(
        "No se entrena un modelo ni se divide train/test en esta etapa. "
        "Antes de entrenar, divide los datos y ajusta el escalador solo "
        "con el conjunto de entrenamiento."
    )


if __name__ == "__main__":
    main()
