import numpy as np

# Array 1D
arr = np.array([10, 20, 30, 40, 50, 60, 70])

# Indexación
print(arr[0])
print(arr[-1])

# Slicing
print(arr[1:4])
print(arr[:3])
print(arr[3:])
print(arr[::2])

# Array 2D
matriz = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

# Indexación: fila 1, columna 2
print(matriz[1, 2])

# Slicing: primeras 2 filas, columnas 1 y 2
print(matriz[:2, 1:3])
