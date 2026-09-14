import numpy as np
import time

# Crear una lista y un array muy grandes
tamano = 1_000_000
lista_grande = list(range(tamano))
array_grande = np.arange(tamano)

# Medir tiempo con lista de Python
inicio = time.time()
lista_resultado = [x * 2 for x in lista_grande]
fin = time.time()

print(f"Tiempo con lista de Python: {fin - inicio:.4f} segundos")

# Medir tiempo con array de NumPy
inicio = time.time()
array_resultado = array_grande * 2
fin = time.time()

print(f"Tiempo con array de NumPy: {fin - inicio:.4f} segundos")
