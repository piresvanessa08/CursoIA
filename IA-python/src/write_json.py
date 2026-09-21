import json

datos = [
    {"nombre": "Café", "hectareas": 5, "produccion_toneladas": 3.2},
    {"nombre": "Caña", "hectareas": 10, "produccion_toneladas": 8.5},
    {"nombre": "Maíz", "hectareas": 3, "produccion_toneladas": 1.8}
]

with open("cultivos_nuevo.json", "w", encoding="utf-8") as archivo:
    json.dump(datos, archivo, ensure_ascii=False, indent=4)

print("Archivo JSON escrito correctamente.")
