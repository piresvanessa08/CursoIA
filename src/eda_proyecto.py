import os
import numpy as np
import matplotlib.pyplot as plt

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
    nombres = [x["nombre"] for x in datos]
    visitantes = [x["visitantes_mes"] for x in datos]

    os.makedirs(output_dir, exist_ok=True)
    
    plt.figure(figsize=(11, 5))
    plt.bar(nombres, visitantes, color='#2b580c', edgecolor='black')
    plt.title("Afluencia de Visitantes por Sitio Turístico en Cartago, Valle", fontsize=12, fontweight='bold')
    plt.xlabel("Sitios Turísticos", fontsize=10)
    plt.ylabel("Visitantes Mensuales", fontsize=10)
    plt.xticks(rotation=30, ha='right', fontsize=9)
    plt.tight_layout()
    
    ruta_imagen = os.path.join(output_dir, "visitantes_sitios.png")
    plt.savefig(ruta_imagen)
    print(f"📈 Gráfico generado exitosamente y guardado en: {ruta_imagen}\n")
    plt.show()