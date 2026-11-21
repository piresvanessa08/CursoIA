import os
import textwrap

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

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
    print(f"Sitios con afluencia documentada: {len(visitantes)}")
    if visitantes.size:
        print(f"Promedio de visitantes mensuales: {np.mean(visitantes):.2f}")
        print(f"Máximo de visitantes en un sitio: {np.max(visitantes):.0f}")
        print(f"Mínimo de visitantes en un sitio: {np.min(visitantes):.0f}")
        print(f"Desviación estándar de visitantes: {np.std(visitantes):.2f}")
    else:
        print("No hay cifras de visitantes verificadas.")
    if calificaciones.size:
        print(f"Calificación promedio general: {np.mean(calificaciones):.2f}")
    else:
        print("No hay calificaciones verificadas.")
    print("=" * 60 + "\n")

def generar_grafico(datos, output_dir="graficos"):
    datos_con_visitantes = [x for x in datos if x["visitantes_mes"] is not None]
    if not datos_con_visitantes:
        print("No se genera el gráfico: no hay cifras de visitantes documentadas.\n")
        return
    nombres = [textwrap.fill(x["nombre"], width=18) for x in datos_con_visitantes]
    visitantes = [x["visitantes_mes"] for x in datos_con_visitantes]
    colores_categoria = {
        "Histórico": "#e74c3c",
        "Cultural": "#e74c3c",
        "Recreativo": "#2ecc71",
        "Religioso": "#f1c40f",
        "Gastronomía": "#3498db",
        "Compras": "#3498db",
    }
    colores = [colores_categoria.get(x["categoria"], "#64748b") for x in datos_con_visitantes]
    bordes = ["#c0392b" if x["precio"] == 0 else "black" for x in datos_con_visitantes]

    os.makedirs(output_dir, exist_ok=True)

    figura, eje = plt.subplots(figsize=(11, 5))
    barras = eje.bar(nombres, visitantes, color=colores, edgecolor=bordes, linewidth=2)
    eje.set_title("Estimación hipotética por sitio — Cartago 2025", fontsize=12, fontweight="bold")
    eje.set_xlabel("Sitios Turísticos", fontsize=13, fontweight="bold", labelpad=14)
    eje.set_ylabel("Visitantes Mensuales", fontsize=10)
    eje.tick_params(axis="x", rotation=0, labelsize=8, pad=8)
    eje.bar_label(barras, labels=[f"{valor:,}" for valor in visitantes], padding=3, fontsize=9, fontweight="bold")
    eje.set_ylim(0, max(visitantes) * 1.15)
    eje.legend(handles=[
        Patch(facecolor="#e74c3c", label="Histórico / Cultural"),
        Patch(facecolor="#2ecc71", label="Recreativo / Natural"),
        Patch(facecolor="#f1c40f", label="Religioso"),
        Patch(facecolor="#3498db", label="Gastronómico / Compras"),
        Patch(facecolor="white", edgecolor="#c0392b", linewidth=2, label="Lugar gratuito"),
    ])
    figura.tight_layout(pad=1.5)
    figura.subplots_adjust(bottom=0.28)

    ruta_imagen = os.path.join(output_dir, "visitantes_sitios.png")
    figura.savefig(ruta_imagen)
    print(f"📈 Gráfico generado exitosamente y guardado en: {ruta_imagen}\n")
    plt.close(figura)
