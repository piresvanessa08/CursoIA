import os
from cargar_datos import leer_datos
from eda_proyecto import mostrar_resumen, generar_grafico
from recomendador import recomendar_con_ia

def main():
    ruta_csv = os.path.join(os.path.dirname(__file__), "..", "data", "sitios_turisticos_cartago.csv")
    
    if not os.path.exists(ruta_csv):
        print(f"❌ Error crítico: No se encontró el archivo de datos en {ruta_csv}")
        return

    datos = leer_datos(ruta_csv)
    mostrar_resumen(datos)
    generar_grafico(datos)
    
    print("\n" + "="*50)
    print("🤖 ¡Bienvenido al Asistente IA de TurismoCartago!")
    print("="*50)
    
    while True:
        print("\n¿Qué tipo de experiencia buscas hoy en Cartago?")
        print("1. Histórico / Cultural")
        print("2. Recreativo / Natural")
        print("3. Religioso")
        print("4. Gastronómico / Compras")
        print("5. Ver exclusivamente lugares gratuitos")
        print("6. Salir del sistema")
        
        # Usamos input() y limpiamos espacios con .strip()
        opcion = input("\nSelecciona el número de tu opción (1-6): ").strip()
        
        if opcion == "6":
            print("\n👋 ¡Gracias por usar TurismoCartago IA! Éxitos en tu presentación. 🌎")
            break
            
        cat_filtro = None
        gratis_filtro = False
        
        if opcion == "1":
            cat_filtro = "Cultural"
        elif opcion == "2":
            cat_filtro = "Recreativo"
        elif opcion == "3":
            cat_filtro = "Religioso"
        elif opcion == "4":
            cat_filtro = "Gastronomia"
        elif opcion == "5":
            gratis_filtro = True
            print("\n🔍 Analizando lugares con acceso gratuito...")
        else:
            print(f"\n❌ Opción no válida ('{opcion}'). Por favor, ingresa un número del 1 al 6.")
            continue
            
        resultados = recomendar_con_ia(datos, categoria_filtro=cat_filtro, solo_gratis=gratis_filtro)
        
        print("\n✨ TOP DE RECOMENDACIONES IA PARA TI:")
        for idx, sitio in enumerate(resultados[:3], 1):
            print(f"\n{idx}. 📌 {sitio['nombre']} ({sitio['categoria']})")
            print(f"   ⭐ Calificación: {sitio['calificacion']} | 💵 Precio: ${sitio['precio']:,.0f}")
            print(f"   ⏰ Horario: {sitio['horario']} | 🎯 Índice de Match: {sitio['compatibilidad']}%")
if __name__ == "__main__":
    main()