import json

try:
    with open("archivo_invalido.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        print(datos)
except json.JSONDecodeError:
    print("Error: el archivo JSON no tiene un formato válido.")
