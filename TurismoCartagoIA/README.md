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
TurismoCartagoIA/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── data/
│   ├── sitios_turisticos_cartago.csv
│   ├── datos_turisticos_limpios.csv
│   └── sitios_turisticos_preparados_ml.csv
├── graficos/
│   ├── visitantes_sitios.png
│   ├── seaborn_distribucion_visitantes.png
│   ├── seaborn_visitantes_categoria.png
│   └── seaborn_visitantes_calificacion.png
├── src/
│   ├── cargar_datos.py
│   ├── eda_proyecto.py
│   ├── main.py
│   ├── preparacion_datos.py
│   └── recomendador.py
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

## Preparación de Datos

La actividad independiente de Pandas y Seaborn se aplica al dataset turístico
del proyecto. Se ejecuta por separado; no cambia el menú de recomendaciones ni
modifica el CSV de entrada:

```powershell
python src\preparacion_datos.py
```

La actividad aplica al dataset turístico las operaciones de la guía: selección
de columnas relevantes, filtrado de sitios con afluencia igual o superior a la
mediana, ordenamiento por visitantes y agrupación por categoría. El resumen de
categorías calcula cantidad de sitios, visitantes totales, promedio de
visitantes y calificación promedio a partir del CSV.

El análisis lee `data/sitios_turisticos_cartago.csv` con Pandas e informa las
primeras y últimas filas, dimensiones, tipos, estadísticas, valores nulos y
duplicados. En el dataset actual hay 7 filas y 6 columnas, no hay valores
nulos ni filas duplicadas. Los valores de visitantes, calificación y precio
son válidos para sus rangos (visitantes y precio no negativos; calificación
entre 0 y 5), por lo que no se imputan ni se alteran. Si aparecen nulos en
otros datos, el script usa mediana para columnas numéricas y moda para las
categóricas. Para nombre u horario ausentes usa `No especificado` para no
atribuir a un sitio la identidad u horario de otro; las filas exactamente
duplicadas se excluyen del archivo limpio.

Se genera `es_gratuito` a partir de `precio` para identificar lugares con
entrada gratuita. Para el archivo de preparación se codifica `categoria` con
One-Hot Encoding; se conservan `visitantes_mes`, `calificacion` y
`es_gratuito` como características numéricas. `precio` no se duplica porque
representa la misma señal que `es_gratuito` para distinguir acceso gratis.
Todavía no se define una variable objetivo ni se entrena o escala un modelo.
El escalado se decidirá al entrenar, después de separar entrenamiento y
prueba, para evitar fuga de información.

Los archivos generados son `data/datos_turisticos_limpios.csv` y
`data/sitios_turisticos_preparados_ml.csv`. Las visualizaciones de Seaborn se
guardan en `graficos/`: distribución de visitantes, promedio de visitantes
por categoría y relación entre visitantes y calificación. El gráfico existente
`graficos/visitantes_sitios.png` se conserva y lo genera la aplicación normal.

En los datos actuales, el promedio mensual es 3057,14 visitantes, con un
mínimo de 1200 (Casa del Virrey) y un máximo de 5000 (Centro Comercial Nuestro
Cartago); la calificación promedio es 4,63. Recreativo registra dos sitios y
las demás categorías uno cada una, así que las comparaciones por categoría
deben leerse como descriptivas y no como conclusiones generales.

El resumen agrupado permite distinguir entre afluencia total y promedio: la
categoría Recreativo suma 6000 visitantes porque tiene dos sitios, mientras
Compras tiene el sitio individual con mayor afluencia (5000). Por el tamaño de
la muestra, la gráfica de dispersión de visitantes y calificación sirve para
explorar los registros, pero no basta para concluir que una variable cause o
prediga la otra.

## Ejecución local

Desde la carpeta `TurismoCartagoIA`:

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

Ejecutar la preparación de datos dentro del contenedor:

```powershell
docker compose run --rm turismo-cartago python src/preparacion_datos.py
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

Para verificar localmente la aplicación y la actividad de preparación, ejecuta
los comandos anteriores desde `TurismoCartagoIA`. La configuración Docker se
puede revisar con `docker compose config` desde esa misma carpeta.
