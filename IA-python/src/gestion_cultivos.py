cultivos = [
    {"nombre": "Café", "hectareas": 5, "produccion_toneladas": 3.2},
    {"nombre": "Caña", "hectareas": 10, "produccion_toneladas": 8.5},
    {"nombre": "Maíz", "hectareas": 3, "produccion_toneladas": 1.8},
    {"nombre": "Plátano", "hectareas": 4, "produccion_toneladas": 6.0},
    {"nombre": "Yuca", "hectareas": 2, "produccion_toneladas": 3.5}
]

def calcular_rendimiento(cultivo):
    return cultivo["produccion_toneladas"] / cultivo["hectareas"]

def mostrar_cultivos(lista_cultivos):
    for cultivo in lista_cultivos:
        rend = calcular_rendimiento(cultivo)
        print(f"{cultivo['nombre']}: {rend:.2f} ton/ha")

def cultivo_mayor_rendimiento(lista_cultivos):
    mejor_cultivo = None
    mayor_rendimiento = -1
    
    for cultivo in lista_cultivos:
        rend = calcular_rendimiento(cultivo)
        if rend > mayor_rendimiento:
            mayor_rendimiento = rend
            mejor_cultivo = cultivo["nombre"]
            
    return mejor_cultivo

if __name__ == "__main__":
    print("--- Reporte de Rendimiento de Cultivos ---")
    mostrar_cultivos(cultivos)
    
    print("\n--- Resultado Destacado ---")
    mejor = cultivo_mayor_rendimiento(cultivos)
    print(f"El cultivo con mayor rendimiento es: {mejor}")