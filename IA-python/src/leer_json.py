import json

with open("cultivos.json", "r", encoding="utf-8") as archivo:
    cultivos = json.load(archivo)

for cultivo in cultivos:
    print(cultivo)
