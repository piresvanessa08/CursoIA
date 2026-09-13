cultivos = [
    {
        "nombre": "Café",
        "hectareas": 5,
        "produccion_toneladas": 3.2
    },
    {
        "nombre": "Caña",
        "hectareas": 10,
        "produccion_toneladas": 8.5
    },
    {
        "nombre": "Maíz",
        "hectareas": 3,
        "produccion_toneladas": 1.8
    },
    {
        "nombre": "Plátano",
        "hectareas": 4,
        "produccion_toneladas": 5.6
    },
    {
        "nombre": "Fríjol",
        "hectareas": 2,
        "produccion_toneladas": 1.4
    }
]


def calcular_rendimiento(cultivo):
    rendimiento = cultivo["produccion_toneladas"] / cultivo["hectareas"]
    return rendimiento


def mostrar_cultivos(lista_cultivos):
    for cultivo in lista_cultivos:
        rendimiento = calcular_rendimiento(cultivo)
        print(
            f"{cultivo['nombre']}: "
            f"{rendimiento:.2f} toneladas por hectárea"
        )


def cultivo_mayor_rendimiento(lista_cultivos):
    mayor_rendimiento = 0
    nombre_mayor_rendimiento = ""

    for cultivo in lista_cultivos:
        rendimiento = calcular_rendimiento(cultivo)

        if rendimiento > mayor_rendimiento:
            mayor_rendimiento = rendimiento
            nombre_mayor_rendimiento = cultivo["nombre"]

    return nombre_mayor_rendimiento


print("Rendimiento de los cultivos en Cartago:")
mostrar_cultivos(cultivos)

mayor = cultivo_mayor_rendimiento(cultivos)

print()
print("Cultivo con mayor rendimiento:", mayor)