import os
import textwrap

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

def mostrar_resumen(datos):
    visitantes = np.array([x["visitantes_mes"] for x in datos])
    calificaciones = np.array([x["calificacion"] for x in datos])

    print("=" * 60)
    print("📊 ANÁLISIS EXPLORATORIO DE DATOS (EDA) - TURISMOCARTAGO IA")
    print("=" * 60)
    print(f"Total de sitios turísticos registrados: {len(datos)}")
    print(f"Promedio de visitantes mensuales: {np.mean(visitantes):.2f}")
    print(f"Máximo de visitantes en un sitio: {np.max(visitantes)}")
    print(f"Mínimo de visitantes en un sitio: {np.min(visitantes)}")
    print(f"Desviación estándar de visitantes: {np.std(visitantes):.2f}")
    print(f"Calificación promedio general: {np.mean(calificaciones):.2f}")
    print("=" * 60 + "\n")

def generar_grafico(datos, output_dir="graficos"):
    nombres = [textwrap.fill(x["nombre"], width=18) for x in datos]
    visitantes = [x["visitantes_mes"] for x in datos]
    colores_categoria = {
        "Histórico": "#e74c3c",
        "Cultural": "#e74c3c",
        "Recreativo": "#2ecc71",
        "Religioso": "#f1c40f",
        "Gastronomía": "#3498db",
        "Compras": "#3498db",
    }
    colores = [colores_categoria[x["categoria"]] for x in datos]
    bordes = ["#c0392b" if x["precio"] == 0 else "black" for x in datos]

    os.makedirs(output_dir, exist_ok=True)
    
    figura, eje = plt.subplots(figsize=(11, 5))
    barras = eje.bar(nombres, visitantes, color=colores, edgecolor=bordes, linewidth=2)
    eje.set_title("Afluencia de Visitantes por Sitio Turístico en Cartago, Valle", fontsize=12, fontweight='bold')
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
    plt.savefig(ruta_imagen)
    print(f"📈 Gráfico generado exitosamente y guardado en: {ruta_imagen}\n")
    plt.show()