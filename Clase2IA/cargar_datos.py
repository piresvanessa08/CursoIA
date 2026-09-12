import csv


def leer_datos(ruta_archivo):
    datos = []

    with open(ruta_archivo, mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            datos.append(fila)

    return datos


def mostrar_resumen(datos):
    valores = []

    for fila in datos:
        valor = float(fila["temperatura"])
        valores.append(valor)

    promedio = sum(valores) / len(valores)
    maximo = max(valores)
    minimo = min(valores)

    print("Cantidad total de registros:", len(datos))
    print("Promedio de temperatura:", promedio)
    print("Temperatura máxima:", maximo)
    print("Temperatura mínima:", minimo)


datos = leer_datos("datos.csv")

mostrar_resumen(datos)