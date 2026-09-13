# cargar_datos.py
import csv

# 1. Función para leer los datos del CSV y convertirlos en diccionarios
def leer_datos(ruta_archivo):
    datos = []
    with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            # Convertimos los valores a números (floats) para poder hacer cálculos
            fila["hectareas"] = float(fila["hectareas"])
            fila["produccion_toneladas"] = float(fila["produccion_toneladas"])
            datos.append(fila)
    return datos

# 2. Función para mostrar resumen estadístico
def mostrar_resumen(datos):
    total_registros = len(datos)
    
    # Extraemos solo las toneladas para hacer los cálculos
    producciones = [cultivo["produccion_toneladas"] for cultivo in datos]
    
    promedio_prod = sum(producciones) / total_registros
    max_prod = max(producciones)
    min_prod = min(producciones)
    
    print("--- Resumen Estadístico de los Datos ---")
    print(f"Cantidad total de registros: {total_registros}")
    print(f"Promedio de producción (toneladas): {promedio_prod:.2f}")
    print(f"Producción máxima: {max_prod}")
    print(f"Producción mínima: {min_prod}")

# --- Ejecución del script ---
ruta = "datos.csv" # Asegúrate de que el archivo se llame así
try:
    mis_datos = leer_datos(ruta)
    mostrar_resumen(mis_datos)
except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{ruta}'. Verifica que esté en la misma carpeta.")