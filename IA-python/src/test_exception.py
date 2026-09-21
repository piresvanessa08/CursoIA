try:
    with open("archivo_que_no_existe.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("Error: el archivo no existe.")
