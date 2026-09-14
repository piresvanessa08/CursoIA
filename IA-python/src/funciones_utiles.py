import numpy as np

# Array de ceros de 2 filas y 3 columnas
ceros = np.zeros((2, 3))
print("Ceros:\n", ceros)

# Array de unos de 3 filas y 2 columnas
unos = np.ones((3, 2))
print("Unos:\n", unos)

# Array de números del 0 al 9
secuencia = np.arange(10)
print("Secuencia:", secuencia)

# 5 números igualmente espaciados entre 0 y 1
espaciados = np.linspace(0, 1, 5)
print("Espaciados:", espaciados)

# Array de números aleatorios
aleatorios = np.random.rand(2, 3)
print("Aleatorios:\n", aleatorios)
