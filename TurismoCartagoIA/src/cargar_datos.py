import csv

def leer_datos(ruta):
    datos = []
    with open(ruta, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            datos.append({
                "nombre": fila["nombre"],
                "categoria": fila["categoria"],
                "visitantes_mes": int(fila["visitantes_mes"]),
                "calificacion": float(fila["calificacion"]),
                "precio": float(fila["precio"]),
                "horario": fila["horario"]
            })
    return datos