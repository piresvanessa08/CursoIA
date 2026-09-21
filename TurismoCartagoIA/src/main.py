import os

from cargar_datos import leer_datos
from eda_proyecto import generar_grafico, mostrar_resumen
from recomendador import recomendar_con_ia


def main():
    proyecto_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta_csv = os.path.join(proyecto_dir, "data", "sitios_turisticos_cartago.csv")
    ruta_graficos = os.path.join(proyecto_dir, "graficos")

    if not os.path.exists(ruta_csv):
        print(f"Error: no se encontro el archivo de datos en {ruta_csv}")
        return

    datos = leer_datos(ruta_csv)
    mostrar_resumen(datos)
    generar_grafico(datos, ruta_graficos)

    print("\n" + "=" * 50)
    print("Bienvenido al Asistente IA de TurismoCartago")
    print("=" * 50)

    while True:
        print("\nQue tipo de experiencia buscas hoy en Cartago?")
        print("1. Historico / Cultural")
        print("2. Recreativo / Natural")
        print("3. Religioso")
        print("4. Gastronomico / Compras")
        print("5. Ver exclusivamente lugares gratuitos")
        print("6. Salir del sistema")

        opcion = input("\nSelecciona el numero de tu opcion (1-6): ").strip()

        if opcion == "6":
            print("\nGracias por usar TurismoCartago IA.")
            break

        categoria_filtro = None
        solo_gratis = False

        if opcion == "1":
            categoria_filtro = ["Histórico", "Cultural"]
        elif opcion == "2":
            categoria_filtro = "Recreativo"
        elif opcion == "3":
            categoria_filtro = "Religioso"
        elif opcion == "4":
            categoria_filtro = ["Gastronomía", "Compras"]
        elif opcion == "5":
            solo_gratis = True
        else:
            print("Opcion no valida. Ingresa un numero del 1 al 6.")
            continue

        resultados = recomendar_con_ia(
            datos,
            categoria_filtro=categoria_filtro,
            solo_gratis=solo_gratis
        )

        print("\nTOP DE RECOMENDACIONES:")
        for indice, sitio in enumerate(resultados[:3], 1):
            print(f"\n{indice}. {sitio['nombre']} ({sitio['categoria']})")
            print(
                f"   Calificacion: {sitio['calificacion']} | "
                f"Precio: ${sitio['precio']:,.0f}"
            )
            print(
                f"   Horario: {sitio['horario']} | "
                f"Compatibilidad: {sitio['compatibilidad']}%"
            )


if __name__ == "__main__":
    main()
