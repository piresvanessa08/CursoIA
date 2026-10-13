from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


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
    print("\nÚltimas filas:")
    print(datos.tail())
    print("\nInformación general:")
    datos.info()
    print("\nTipos de datos:")
    print(datos.dtypes)
    print("\nEstadísticas descriptivas:")
    print(datos.describe(include="all"))
    print("\nValores nulos por columna:")
    print(datos.isnull().sum())
    print(f"\nFilas duplicadas: {datos.duplicated().sum()}")


def analizar_operaciones_pandas(datos):
    """Demuestra selección, filtrado, agrupación y ordenamiento con datos reales."""
    columnas_clave = datos[["nombre", "categoria", "visitantes_mes", "calificacion"]]
    print("\nColumnas seleccionadas para analizar los sitios:")
    print(columnas_clave.head())

    umbral_visitantes = datos["visitantes_mes"].median()
    sitios_mayor_afluencia = datos.loc[
        datos["visitantes_mes"] >= umbral_visitantes,
        ["nombre", "categoria", "visitantes_mes"],
    ].sort_values("visitantes_mes", ascending=False)
    print(
        "\nSitios con visitantes iguales o superiores a la mediana "
        f"({umbral_visitantes:.0f}), ordenados de mayor a menor:"
    )
    print(sitios_mayor_afluencia.to_string(index=False))

    resumen_categorias = (
        datos.groupby("categoria", as_index=False)
        .agg(
            cantidad_sitios=("nombre", "count"),
            visitantes_totales=("visitantes_mes", "sum"),
            promedio_visitantes=("visitantes_mes", "mean"),
            calificacion_promedio=("calificacion", "mean"),
        )
        .sort_values("visitantes_totales", ascending=False)
    )
    print("\nResumen por categoría, ordenado por visitantes totales:")
    print(resumen_categorias.to_string(index=False, formatters={
        "promedio_visitantes": "{:,.2f}".format,
        "calificacion_promedio": "{:.2f}".format,
    }))


def limpiar_datos(datos):
    datos_limpios = datos.copy()

    duplicados = datos_limpios.duplicated()
    if duplicados.any():
        print(f"Filas duplicadas detectadas y excluidas: {int(duplicados.sum())}")
        datos_limpios = datos_limpios.loc[~duplicados].copy()
    else:
        print("No se encontraron filas duplicadas.")

    for columna in NUMERIC_COLUMNS:
        datos_limpios[columna] = pd.to_numeric(datos_limpios[columna], errors="coerce")

    limites = {
        "visitantes_mes": datos_limpios["visitantes_mes"] < 0,
        "calificacion": datos_limpios["calificacion"].notna()
        & ~datos_limpios["calificacion"].between(0, 5),
        "precio": datos_limpios["precio"] < 0,
    }
    for columna, invalidos in limites.items():
        if invalidos.any():
            raise ValueError(f"Hay valores imposibles o inconsistentes en '{columna}'.")

    for columna in datos_limpios.columns:
        if not datos_limpios[columna].isnull().any():
            continue

        if pd.api.types.is_numeric_dtype(datos_limpios[columna]):
            valor_relleno = datos_limpios[columna].median()
        elif columna in {"nombre", "horario"}:
            valor_relleno = "No especificado"
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

    return datos_limpios


def agregar_caracteristicas(datos):
    """Añade un indicador derivado sin modificar la fuente original."""
    resultado = datos.copy()
    resultado["es_gratuito"] = resultado["precio"].eq(0).astype(int)
    return resultado


def visualizar_datos(datos, output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    sns.set_theme(style="whitegrid")

    figura, eje = plt.subplots(figsize=(8, 5))
    sns.histplot(data=datos, x="visitantes_mes", bins="auto", kde=True, ax=eje)
    eje.set_title("Distribución de visitantes mensuales por sitio")
    eje.set_xlabel("Visitantes mensuales (personas)")
    eje.set_ylabel("Cantidad de sitios")
    figura.tight_layout()
    figura.savefig(output_dir / "seaborn_distribucion_visitantes.png", dpi=150)
    plt.close(figura)

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
    # precio y es_gratuito representan la misma información; se evita duplicarla.
    datos_ml = datos[["categoria", "visitantes_mes", "calificacion", "es_gratuito"]].copy()
    datos_ml = pd.get_dummies(
        datos_ml,
        columns=["categoria"],
        prefix="categoria",
        dtype=int,
    )

    if datos_ml.isnull().any().any():
        raise ValueError("El conjunto preparado conserva valores faltantes.")
    if not all(pd.api.types.is_numeric_dtype(tipo) for tipo in datos_ml.dtypes):
        raise ValueError("El conjunto preparado contiene columnas no numéricas.")
    return datos_ml


def main():
    datos = cargar_datos(DATA_PATH)
    explorar_datos(datos)
    analizar_operaciones_pandas(datos)

    datos_limpios = limpiar_datos(datos)
    datos_limpios = agregar_caracteristicas(datos_limpios)
    ruta_limpios = PROJECT_DIR / "data" / "datos_turisticos_limpios.csv"
    datos_limpios.to_csv(ruta_limpios, index=False)
    print(f"\nDatos limpios guardados en: {ruta_limpios}")

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
