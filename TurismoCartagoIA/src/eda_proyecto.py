import os
import textwrap

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.ticker import FuncFormatter

def mostrar_resumen(datos):
    visitantes = np.array(
        [x["visitantes_mes"] for x in datos if x["visitantes_mes"] is not None],
        dtype=float,
    )
    calificaciones = np.array(
        [x["calificacion"] for x in datos if x["calificacion"] is not None],
        dtype=float,
    )

    print("=" * 60)
    print("📊 ANÁLISIS EXPLORATORIO DE DATOS (EDA) - TURISMOCARTAGO IA")
    print("=" * 60)
    print(f"Total de sitios turísticos registrados: {len(datos)}")
    print(f"Sitios con visitantes registrados: {len(visitantes)}")
    if visitantes.size:
        print(f"Promedio de visitantes mensuales: {np.mean(visitantes):.2f}")
        print(f"Máximo de visitantes en un sitio: {np.max(visitantes):.0f}")
        print(f"Mínimo de visitantes en un sitio: {np.min(visitantes):.0f}")
        print(f"Desviación estándar de visitantes: {np.std(visitantes):.2f}")
    else:
        print("No hay registros de visitantes.")
    if calificaciones.size:
        print(f"Calificación promedio general: {np.mean(calificaciones):.2f}")
    else:
        print("No hay calificaciones registradas.")
    print("=" * 60 + "\n")

def generar_grafico(datos, output_dir="graficos"):
    datos_con_visitantes = [x for x in datos if x["visitantes_mes"] is not None]
    if not datos_con_visitantes:
        print("No se genera el gráfico: no hay registros de visitantes.\n")
        return
    datos_ordenados = sorted(
        datos_con_visitantes,
        key=lambda sitio: sitio["visitantes_mes"],
        reverse=True,
    )
    colores_categoria = {
        "Histórico": "#b23a48",
        "Cultural": "#7251a3",
        "Recreativo": "#27845b",
        "Religioso": "#d49200",
        "Gastronomía": "#2878a5",
        "Compras": "#d65a31",
    }
    nombres = [
        textwrap.fill(
            f"{sitio['nombre']}{' [Gratis]' if sitio['precio'] == 0 else ''}",
            width=45,
        )
        for sitio in datos_ordenados
    ]
    visitantes = [sitio["visitantes_mes"] for sitio in datos_ordenados]
    colores = [
        colores_categoria.get(sitio["categoria"], "#64748b")
        for sitio in datos_ordenados
    ]

    os.makedirs(output_dir, exist_ok=True)

    figura, eje = plt.subplots(figsize=(12, max(10, len(datos_ordenados) * 0.38)))
    posiciones = np.arange(len(datos_ordenados))
    barras = eje.barh(posiciones, visitantes, color=colores, height=0.72)
    eje.set_yticks(posiciones, labels=nombres, fontsize=8.5)
    eje.invert_yaxis()
    eje.set_title("Atractivos turísticos", loc="left", fontsize=10, pad=12)
    eje.set_xlabel("Visitantes estimados al mes", fontweight="bold")
    eje.xaxis.set_major_formatter(
        FuncFormatter(lambda valor, _: f"{valor:,.0f}".replace(",", "."))
    )
    eje.bar_label(
        barras,
        labels=[f"{valor:,.0f}".replace(",", ".") for valor in visitantes],
        padding=4,
        fontsize=8,
        fontweight="bold",
    )
    eje.set_xlim(0, max(visitantes) * 1.15)
    eje.set_axisbelow(True)
    eje.grid(axis="x", color="#dbe2ea", linestyle="--", alpha=0.75)
    eje.spines[["top", "right", "left"]].set_visible(False)
    figura.suptitle(
        "Afluencia mensual estimada por atractivo — Cartago 2025",
        fontsize=16,
        fontweight="bold",
        y=0.99,
    )
    categorias = [
        "Histórico",
        "Cultural",
        "Recreativo",
        "Religioso",
        "Gastronomía",
        "Compras",
    ]
    figura.legend(
        handles=[
            Patch(facecolor=colores_categoria[categoria], label=categoria)
            for categoria in categorias
        ],
        title="Categoría",
        loc="upper center",
        bbox_to_anchor=(0.68, 0.96),
        ncol=3,
        frameon=False,
        fontsize=9,
    )
    figura.text(
        0.68,
        0.875,
        "[Gratis] indica precio de entrada igual a $0",
        ha="center",
        fontsize=9,
    )
    figura.subplots_adjust(left=0.37, right=0.97, top=0.82, bottom=0.04)

    ruta_imagen = os.path.join(output_dir, "visitantes_sitios.png")
    figura.savefig(ruta_imagen, dpi=180, bbox_inches="tight")
    print(f"Gráfico generado y guardado en: {ruta_imagen}\n")
    plt.close(figura)
