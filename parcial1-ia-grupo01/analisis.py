import csv
import numpy as np

with open("grupo_01.txt", "r", encoding="utf-8") as archivo:
    datos = list(csv.DictReader(archivo))

print("=== CARGA DE DATOS ===")
print("Primeros 5 registros:")
for fila in datos[:5]:
    print(fila)

print("\nTotal de registros:", len(datos))


hectareas = np.array([
    float(fila["hectareas"])
    for fila in datos
])

altitudes = np.array([
    float(fila["altitud_msnm"])
    for fila in datos
])

produccion = np.array([
    float(fila["produccion_kg"])
    for fila in datos
    if fila["produccion_kg"] != ""
])


print("\n=== ESTADÍSTICAS DE PRODUCCIÓN ===")
print("Cantidad de datos:", len(produccion))
print("Media:", np.mean(produccion))
print("Mediana:", np.median(produccion))
print("Desviación estándar:", np.std(produccion))
print("Mínimo:", np.min(produccion))
print("Máximo:", np.max(produccion))


print("\n=== CALIDAD DE LOS DATOS ===")

faltantes = sum(
    1 for fila in datos
    if fila["produccion_kg"] == ""
)

print("Valores faltantes en producción:", faltantes)

print("Producción máxima encontrada:", np.max(produccion))

print("Posible valor atípico: 51000 kg")

print("Finca repetida: La Esperanza")

produccion_sin_atipico = produccion[produccion != 51000]

print("\n=== ANÁLISIS DEL VALOR ATÍPICO ===")
print("Media sin el valor atípico:", np.mean(produccion_sin_atipico))
print("Mediana sin el valor atípico:", np.median(produccion_sin_atipico))
print("Desviación estándar sin el valor atípico:", np.std(produccion_sin_atipico))

print("\n=== INTERPRETACIÓN ===")
print("La media es mayor que la mediana debido principalmente al valor atípico de 51000 kg.")
print("La mediana representa mejor la producción típica de las fincas.")

import matplotlib.pyplot as plt

# === GRÁFICO 1: DISTRIBUCIÓN DE LA PRODUCCIÓN ===
plt.figure(figsize=(8, 5))
plt.hist(produccion, bins=8)
plt.title("Distribución de la producción de café")
plt.xlabel("Producción (kg)")
plt.ylabel("Cantidad de fincas")
plt.tight_layout()
plt.savefig("graficos/distribucion_produccion.png")
plt.close()


# === GRÁFICO 2: HECTÁREAS VS PRODUCCIÓN ===
# Usamos únicamente los registros que tienen producción
hectareas_completas = np.array([
    float(fila["hectareas"])
    for fila in datos
    if fila["produccion_kg"] != ""
])

plt.figure(figsize=(8, 5))
plt.scatter(hectareas_completas, produccion)
plt.title("Relación entre hectáreas y producción")
plt.xlabel("Hectáreas")
plt.ylabel("Producción (kg)")
plt.tight_layout()
plt.savefig("graficos/hectareas_vs_produccion.png")
plt.close()

print("\n=== GRÁFICOS ===")
print("Gráfico 1 guardado: graficos/distribucion_produccion.png")
print("Gráfico 2 guardado: graficos/hectareas_vs_produccion.png")

correlacion = np.corrcoef(hectareas_completas, produccion)[0, 1]

print("\n=== CORRELACIÓN ===")
print("Correlación entre hectáreas y producción:", correlacion)

if correlacion > 0:
    print("Existe una relación positiva: en general, al aumentar las hectáreas también aumenta la producción.")
elif correlacion < 0:
    print("Existe una relación negativa.")
else:
    print("No existe una relación lineal.")
    
print("La correlación no demuestra que las hectáreas causen directamente una mayor producción.")
# === INTERPRETACIÓN PROFUNDA ===

print("\n=== INTERPRETACIÓN PROFUNDA ===")
print("1. La producción presenta una distribución muy afectada por el valor de 51000 kg.")
print("2. La mediana de 2950 kg representa mejor una producción típica que la media de 7041.67 kg.")
print("3. Sin el valor atípico, la media baja a 3045.45 kg.")
print("4. La relación entre hectáreas y producción es positiva y moderada (r = 0.52).")
print("5. Esta relación no implica causalidad, porque pueden existir otros factores como variedad,")
print("   altitud, clima, suelo y manejo de la finca.")

# === RECOMENDACIÓN ===

print("\n=== RECOMENDACIÓN ===")
print("Se recomienda validar los datos antes de tomar decisiones agrícolas.")
print("Se debe revisar especialmente el registro de La Montaña, que reporta 51000 kg,")
print("completar el dato faltante de El Roble y verificar la identificación repetida de La Esperanza.")
print("También se recomienda registrar información adicional sobre variedad, clima, suelo")
print("y manejo agrícola para explicar mejor las diferencias de producción.")