# Lista de diccionarios con cultivos
cultivos = [
    {"nombre": "Café", "hectareas": 5, "produccion_toneladas": 3.2},
    {"nombre": "Caña", "hectareas": 10, "produccion_toneladas": 8.5},
    {"nombre": "Maíz", "hectareas": 3, "produccion_toneladas": 1.8},
    {"nombre": "Plátano", "hectareas": 4, "produccion_toneladas": 6.0},
    {"nombre": "Yuca", "hectareas": 2, "produccion_toneladas": 2.5}
]

def calcular_rendimiento(cultivo):
    return cultivo["produccion_toneladas"] / cultivo["hectareas"]

def mostrar_cultivos(lista_cultivos):
    for c in lista_cultivos:
        rend = calcular_rendimiento(c)
        print(f"Cultivo: {c['nombre']} - Rendimiento: {rend:.2f} ton/ha")

def cultivo_mayor_rendimiento(lista_cultivos):
    mayor = max(lista_cultivos, key=calcular_rendimiento)
    return mayor["nombre"]

# Programa principal
print("--- LISTA DE CULTIVOS Y RENDIMIENTOS ---")
mostrar_cultivos(cultivos)

mejor = cultivo_mayor_rendimiento(cultivos)
print(f"\nEl cultivo con mayor rendimiento es: {mejor}")