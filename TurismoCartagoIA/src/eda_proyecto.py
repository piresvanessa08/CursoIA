import os

import matplotlib.pyplot as plt
import numpy as np


def mostrar_resumen(datos):
    visitantes = np.array([sitio["visitantes_mes"] for sitio in datos])
    calificaciones = np.array([sitio["calificacion"] for sitio in datos])

    print("=" * 60)
    print("ANALISIS EXPLORATORIO DE DATOS (EDA) - TURISMOCARTAGO IA")
    print("=" * 60)
    print(f"Total de sitios turisticos registrados: {len(datos)}")
    print(f"Promedio de visitantes mensuales: {np.mean(visitantes):.2f}")
    print(f"Maximo de visitantes en un sitio: {np.max(visitantes)}")
    print(f"Minimo de visitantes en un sitio: {np.min(visitantes)}")
    print(f"Desviacion estandar de visitantes: {np.std(visitantes):.2f}")
    print(f"Calificacion promedio general: {np.mean(calificaciones):.2f}")
    print("=" * 60 + "\n")


def generar_grafico(datos, output_dir="graficos"):
    nombres = [sitio["nombre"] for sitio in datos]
    visitantes = [sitio["visitantes_mes"] for sitio in datos]

    os.makedirs(output_dir, exist_ok=True)

    plt.close("all")
    figura, eje = plt.subplots(figsize=(11, 5))
    eje.bar(nombres, visitantes, color="#2b580c", edgecolor="black")
    eje.set_title("Afluencia de Visitantes por Sitio Turistico en Cartago, Valle")
    eje.set_xlabel("Sitios Turisticos")
    eje.set_ylabel("Visitantes Mensuales")
    eje.tick_params(axis="x", rotation=30, labelsize=9)
    figura.tight_layout()

    ruta_imagen = os.path.join(output_dir, "visitantes_sitios.png")
    figura.savefig(ruta_imagen)
    print(f"Grafico generado exitosamente y guardado en: {ruta_imagen}\n")
    plt.show(block=True)
    plt.close(figura)
