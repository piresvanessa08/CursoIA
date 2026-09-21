import csv

def leer_datos(ruta_archivo):
    lista_datos = []
    try:
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                lista_datos.append(fila)
    except FileNotFoundError:
        print(f"No se encontró el archivo en la ruta: {ruta_archivo}")
    return lista_datos

def mostrar_resumen(datos):
    total_registros = len(datos)
    print(f"Cantidad total de registros: {total_registros}")
    if total_registros > 0:
        print("Datos cargados exitosamente listos para procesar.")


