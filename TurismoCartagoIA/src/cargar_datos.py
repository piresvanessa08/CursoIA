import csv


def _numero_opcional(valor, tipo):
    valor = (valor or "").strip()
    return None if not valor else tipo(valor)

def leer_datos(ruta):
    datos = []
    with open(ruta, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            datos.append({
                "nombre": fila["nombre"],
                "categoria": fila["categoria"],
                "visitantes_mes": _numero_opcional(fila.get("visitantes_mes"), int),
                "calificacion": _numero_opcional(fila.get("calificacion"), float),
                "precio": _numero_opcional(fila.get("precio"), float),
                "horario": fila.get("horario") or "No verificado",
                "fuente": fila.get("fuente") or "",
                "datos_estimados": (fila.get("datos_estimados") or "0").strip() == "1",
            })
    return datos
