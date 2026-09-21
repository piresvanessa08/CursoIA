import csv

datos = [
    ["nombre", "hectareas", "produccion_toneladas"],
    ["Café", 5, 3.2],
    ["Caña", 10, 8.5],
]

with open("cultivos_nuevo.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(datos)

print("Archivo CSV escrito correctamente.")
