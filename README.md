# TurismoCartago IA 🌎🤖

Repositorio oficial para el avance del primer corte del proyecto de Inteligencia Artificial.

## 📌 A. Definición del Proyecto
* **Nombre del proyecto:** TurismoCartago IA
* **Problemática:** Los ciudadanos y turistas en Cartago, Valle del Cauca, carecen de una herramienta analítica y automatizada que permita conocer la afluencia real, categorías y características de los sitios turísticos de la ciudad para planificar mejores experiencias[cite: 1, 2].
* **Objetivo:** Desarrollar un sistema en Python que procese datos turísticos locales, ejecute un análisis exploratorio (EDA) con NumPy y provea un recomendador inteligente basado en preferencias de los usuarios[cite: 1, 2].
* **Datos:** Dataset estructurado de manera propia basado en 7 sitios turísticos oficiales de Cartago (incluyendo Parque de Bolívar, Casa del Virrey, Parque de la Isleta, entre otros) con información de categorías, visitantes mensuales, calificaciones, precios y horarios.

## 📂 B. Estructura de Datos
* Archivo principal de datos: `sitios_turisticos_cartago.csv` cargado mediante lectura de archivos en Python.
* Procesamiento de datos implementado mediante **listas de diccionarios**.
* Funciones definidas en el código para lectura, análisis estadístico y recomendación.

## 📊 C. Análisis Exploratorio de Datos (EDA)
* **Herramientas:** Uso de **NumPy** para cálculos estadísticos (promedio, máximo, mínimo y desviación estándar de visitantes) y **Matplotlib** para la generación de gráficos de barras de afluencia[cite: 1, 2].
* **Hallazgos clave:**
  1. *Afluencia Comercial y Religiosa:* El Centro Comercial Nuestro Cartago (5,000 visitantes/mes) y la Catedral Nuestra Señora del Carmen (4,200 visitantes/mes) concentran la mayor afluencia de la ciudad.
  2. *Potencial Cultural:* La Casa del Virrey destaca por poseer la calificación más alta (4.9 estrellas), pero registra una menor afluencia (1,200 visitantes), lo que señala una oportunidad clave para impulsar el turismo histórico-cultural.

## 🛠️ D. Instrucciones de Ejecución
1. Asegúrate de tener instaladas las librerías requeridas:
   ```bash
   pip install numpy matplotlib