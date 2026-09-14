import numpy as np

# Crear datos de ejemplo (temperaturas en Cartago)
temperaturas = np.array([28, 30, 25, 27, 29, 31, 26, 24, 32, 28])

# Estadísticas básicas
media = np.mean(temperaturas)
mediana = np.median(temperaturas)
desviacion = np.std(temperaturas)
maximo = np.max(temperaturas)
minimo = np.min(temperaturas)

print(f"Media: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Desviación estándar: {desviacion:.2f}")
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")
