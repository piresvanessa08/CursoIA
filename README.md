# TurismoCartago IA

Proyecto académico de Inteligencia Artificial para analizar sitios turísticos de
Cartago, Valle del Cauca, y generar recomendaciones según las preferencias del
usuario.

## Objetivos

- Leer y procesar los datos turísticos desde un archivo CSV.
- Calcular estadísticas de visitantes y calificaciones con NumPy.
- Generar una gráfica de afluencia con Matplotlib.
- Recomendar sitios por categoría o por acceso gratuito.
- Ejecutar el proyecto localmente o dentro de Docker.

## Tecnologías

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Docker
- Docker Compose
- Git y GitHub

## Estructura

```text
CursoIA/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── data/
│   └── sitios_turisticos_cartago.csv
├── graficos/
│   └── visitantes_sitios.png
├── src/
│   ├── cargar_datos.py
│   ├── eda_proyecto.py
│   ├── main.py
│   ├── preparacion_datos.py
│   └── recomendador.py
└── tests/
```

## Datos

El archivo `data/sitios_turisticos_cartago.csv` contiene siete sitios con
nombre, categoría, visitantes mensuales, calificación, precio y horario.
Entre los registros se encuentra Restaurante Casa Vieja, de categoría
Gastronomía, con horario de 12:00 m a 9:00 p.m.

## Análisis y gráfica

El programa calcula el total de sitios, promedio, máximo, mínimo y desviación
estándar de visitantes, además del promedio general de calificaciones.

La gráfica se guarda en:

```text
graficos/visitantes_sitios.png
```

Las barras utilizan colores por categoría y muestran el número de visitantes
encima de cada barra.

## Exploración y preparación para Machine Learning

La aplicación principal y su recomendador siguen funcionando como antes.
Para ejecutar por separado la actividad basada en Pandas y Seaborn:

```powershell
python src\preparacion_datos.py
```

El script muestra dimensiones, tipos de datos, estadísticas, valores nulos y
duplicados; elimina duplicados e imputa valores faltantes con la mediana para
columnas numéricas o la moda para columnas de texto. Genera gráficos
adicionales en `graficos/` y guarda un CSV codificado y escalado en
`data/sitios_turisticos_preparados_ml.csv`. No modifica el CSV original ni
entrena un modelo. Este resultado es una demostración de preparación: cuando
se entrene un modelo, la división train/test debe hacerse antes de ajustar el
escalador, usando solo los datos de entrenamiento. La división queda para la
siguiente clase, tal como indica la guía.

## Ejecución local

Desde la carpeta raíz del proyecto:

```powershell
python src\main.py
```

El menú ofrece estas opciones:

1. Histórico / Cultural
2. Recreativo / Natural
3. Religioso
4. Gastronómico / Compras
5. Lugares gratuitos
6. Salir

## Ejecución con Docker

Construir la imagen:

```powershell
docker compose build
```

Ejecutar el programa:

```powershell
docker compose run --rm turismo-cartago
```

Detener servicios activos:

```powershell
docker compose down
```

La gráfica se guarda en la carpeta `graficos` del proyecto porque Docker monta
la carpeta local como volumen.

## Comprobaciones

Para confirmar que Docker funciona:

```powershell
docker run hello-world
docker compose build
docker compose run --rm turismo-cartago
```

El proyecto fue probado con ejecución local y dentro de Docker. La rama
principal se encuentra sincronizada con el repositorio de GitHub.