# TurismoCartagoIA

Proyecto académico de Inteligencia Artificial para analizar sitios turísticos de Cartago, Valle del Cauca, y generar recomendaciones según las preferencias del usuario.

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

## Estructura del proyecto

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
│   ├── perceptron_proyecto.py
│   ├── preparacion_datos.py
│   └── recomendador.py
└── tests/
    └── test_perceptron_proyecto.py
```

## Datos

El archivo `data/sitios_turisticos_cartago.csv` contiene siete sitios con nombre, categoría, visitantes mensuales, calificación, precio y horario.

Entre los registros se encuentra Restaurante Casa Vieja, de categoría Gastronomía, con horario de 12:00 m. a 9:00 p. m.

## Análisis y gráfica

El programa calcula el total de sitios, el promedio, el máximo, el mínimo y la desviación estándar de visitantes, además del promedio general de calificaciones.

La gráfica se guarda en:

`graficos/visitantes_sitios.png`

Las barras utilizan colores por categoría y muestran el número de visitantes encima de cada barra.

## Preparación de datos

La actividad independiente de Pandas y Seaborn se aplica al conjunto de datos turísticos del proyecto. Se ejecuta por separado; no cambia el menú de recomendaciones ni modifica el CSV de entrada.

```bash
python src/preparacion_datos.py
```

La actividad aplica al conjunto de datos turístico las operaciones de la guía: selección de columnas relevantes, filtrado de sitios con afluencia igual o superior a la mediana, ordenamiento por visitantes y agrupación por categoría. El resumen de categorías calcula la cantidad de sitios, los visitantes totales, el promedio de visitantes y la calificación promedio a partir del CSV.

El análisis lee `data/sitios_turisticos_cartago.csv` con Pandas e informa las primeras y últimas filas, dimensiones, tipos de datos, estadísticas, valores nulos y duplicados.

En el conjunto de datos actual hay siete filas y seis columnas, sin valores nulos ni filas duplicadas. Los valores de visitantes, calificación y precio están dentro de los rangos definidos: visitantes y precio no negativos, y calificación entre 0 y 5. Por ello, no se imputan ni se alteran estos valores.

Si aparecen valores nulos en otros datos, el script utiliza la mediana para columnas numéricas y la moda para las categóricas. Para nombres u horarios ausentes utiliza `No especificado`, sin atribuir a un sitio la identidad u horario de otro. Las filas exactamente duplicadas se excluyen del archivo limpio.

Se genera `es_gratuito` a partir de `precio` para identificar lugares con entrada gratuita. Para el archivo de preparación se codifica `categoria` mediante One-Hot Encoding. Se conservan `visitantes_mes` y `calificacion` como columnas numéricas. `precio` no se duplica como característica porque se utiliza el indicador `es_gratuito` para distinguir el acceso gratuito.

Los archivos generados son:

- `data/datos_turisticos_limpios.csv`
- `data/sitios_turisticos_preparados_ml.csv`

Las visualizaciones de Seaborn se guardan en `graficos/`: distribución de visitantes, promedio de visitantes por categoría, relación entre visitantes y calificación, y relación entre las entradas del perceptrón y su objetivo. La gráfica existente `graficos/visitantes_sitios.png` se conserva y la genera la aplicación normal.

En los datos actuales, el promedio mensual es de 3057,14 visitantes, con un mínimo de 1200 (Casa del Virrey) y un máximo de 5000 (Centro Comercial Nuestro Cartago). La calificación promedio es de 4,63.

La categoría Recreativo registra dos sitios y las demás categorías uno cada una, por lo que las comparaciones por categoría deben interpretarse como descriptivas y no como conclusiones generales.

El resumen agrupado permite distinguir entre afluencia total y promedio: la categoría Recreativo suma 6000 visitantes porque tiene dos sitios, mientras que Compras tiene el sitio individual con mayor afluencia (5000). Por el tamaño de la muestra, la gráfica de dispersión de visitantes y calificación sirve para explorar los registros, pero no basta para concluir que una variable causa o predice la otra.

## Avance 2

La preparación de datos y el perceptrón son actividades independientes: no cambian el CSV original, el menú ni el recomendador.

Para generar los datos limpios, los gráficos de Seaborn y el CSV codificado:

```bash
python src/preparacion_datos.py
```

### Objetivo y entradas del perceptrón

El script `src/perceptron_proyecto.py` entrena desde cero, utilizando NumPy, un modelo logístico de dos entradas.

Para esta demostración académica, la clase positiva se define como `visitantes_mes >= mediana`. La mediana de los siete registros actuales es de 3200 visitantes mensuales. `visitantes_mes` define la etiqueta y, por eso, no se utiliza como entrada.

Las entradas son `calificacion` y `es_gratuito`, estandarizadas con la media y la desviación estándar del conjunto. El script implementa el sigmoide, la pérdida logarítmica y el descenso del gradiente sin utilizar Scikit-Learn.

### Ajustes, tabla y análisis visual

No se recibieron observaciones específicas sobre la sustentación del Avance 1; por tanto, no se atribuyen cambios a comentarios inexistentes. Este avance documenta por separado el trabajo de preparación de datos, visualización y modelo solicitado en la guía.

En el CSV original hay siete filas, seis columnas, cero valores nulos y cero duplicados. La limpieza no elimina ni imputa registros porque no se encontraron problemas en esos datos. El archivo limpio añade el indicador derivado `es_gratuito`; la tabla codificada para explorar aprendizaje automático agrega las columnas One-Hot de categoría.

| Etapa | Filas | Columnas | Nulos | Duplicados |
|---|---:|---:|---:|---:|
| CSV original | 7 | 6 | 0 | 0 |
| CSV limpio, con `es_gratuito` | 7 | 7 | 0 | 0 |
| CSV preparado, con categorías codificadas | 7 | 9 | 0 | 0 |

**Nota:** verifica que el número de columnas del CSV preparado coincida con el archivo que genera realmente el script, ya que depende de las categorías codificadas y de las columnas conservadas.

La información turística se consultó en las fuentes de la sección Referencias. La relación exacta entre cada valor del CSV (visitantes por sitio, calificaciones y precios) y una tabla o página concreta de esas fuentes aún debe cotejarse antes de presentar cada valor como una transcripción directa. La publicación de Facebook se conserva solo como referencia complementaria, no como fuente estadística primaria.

### Interpretación de los gráficos de Seaborn

- **Distribución de visitantes:** muestra registros entre 1200 y 5000 visitantes mensuales. La muestra es pequeña y el histograma describe estos siete sitios, no la demanda turística completa.
- **Visitantes promedio por categoría:** Compras tiene 5000 visitantes y Recreativo promedia 3000 entre sus dos sitios. Las demás categorías tienen un solo registro, por lo que las diferencias no son generalizables.
- **Visitantes y calificación:** Casa del Virrey combina la menor afluencia (1200) con una calificación de 4,9; el centro comercial combina la mayor afluencia (5000) con 4,3. Esto no prueba una relación causal o predictiva.
- **Entradas y objetivo:** `seaborn_entradas_objetivo.png` compara la calificación y el acceso gratuito entre las clases de afluencia inferior a la mediana y de afluencia igual o superior a 3200 visitantes. Siete registros no bastan para establecer una regla predictiva confiable.

### Ejecución local del perceptrón

Desde la carpeta `TurismoCartagoIA`:

```bash
python src/perceptron_proyecto.py
```

El programa informa los dos pesos, el sesgo, las pérdidas inicial y final y la exactitud sobre los mismos siete registros utilizados para entrenar. También genera:

- `graficos/perceptron_curva_aprendizaje.png`
- `graficos/perceptron_frontera_decision.png`

En la ejecución de referencia, la pérdida baja de 0,693147 a 0,287596 y la exactitud del entrenamiento es de 85,71 %. Ambos pesos son positivos en esta ejecución: dentro de este ajuste, una calificación estandarizada mayor y el acceso gratuito se asocian con una probabilidad estimada mayor de pertenecer a la clase de alta afluencia. Esto no demuestra causalidad.

La frontera lineal no separa perfectamente los registros: queda al menos un error de clasificación en la ejecución de referencia.

**Limitación:** siete observaciones no permiten una evaluación independiente ni conclusiones generalizables. La exactitud informada es de entrenamiento; se presenta solo para demostrar el algoritmo solicitado, no como rendimiento predictivo validado. Los datos de entrada del proyecto no incluyen una referencia trazable por fila para los valores de visitantes, calificaciones y precios; la verificación de la tabla o página de origen y del período de cada métrica queda pendiente antes de presentar resultados como evidencia real.

Los gráficos y archivos de datos se generan a partir de la fuente CSV; el script del perceptrón no cambia ese archivo.

## Plan hacia el proyecto final

El problema de esta demostración es de clasificación binaria: distinguir entre afluencia menor a la mediana y afluencia igual o mayor a la mediana.

Para la comparación de la Clase 12 se propone evaluar la regresión logística y el árbol de decisión con la métrica de precisión equilibrada (*balanced accuracy*), para considerar el desempeño de ambas clases.

Antes de comparar modelos formalmente, se deben ampliar y documentar los datos. Siete registros no permiten una partición de prueba ni una validación cruzada que respalde conclusiones. El calendario y los casos nuevos de demostración se completarán en el documento de entrega cuando se confirmen con el grupo.

## Ejecución local

Desde la carpeta `TurismoCartagoIA`:

```bash
python src/main.py
```

El menú ofrece estas opciones:

- Histórico / Cultural
- Recreativo / Natural
- Religioso
- Gastronómico / Compras
- Lugares gratuitos
- Salir

## Referencias

Fuentes compartidas por la autora del proyecto; consultadas el 22 de octubre de 2026:

- SITUR Valle. (s. f.). *Estadísticas*. https://siturvalle.com/estadisticas/
- Municipio de Cartago. (2022). *Anuario Estadístico – Cartago 2022*. https://cartago.gov.co/anuario-estadistico-cartago-2022/
- Publicación de Facebook sobre visitantes alojados en Cartago durante Semana Santa. (s. f.). Referencia complementaria; no se usa como fuente primaria para entrenar o validar el modelo. https://www.facebook.com/100007741248027/photos/cartago-la-ciudad-del-valle-que-m%C3%A1s-turistas-aloj%C3%B3-en-la-semana-santa-seg%C3%BAn-dato/2931266880474658/

## Comprobaciones

Verificar que Docker está instalado y funciona:

```bash
docker run hello-world
```

Validar la configuración de Docker Compose:

```bash
docker compose config
```

Ejecutar las pruebas automatizadas desde la carpeta `TurismoCartagoIA`:

```bash
python -m unittest discover -s tests -v
```

Las pruebas permiten comprobar que los casos incluidos en la suite funcionan correctamente en el entorno local.

## Ejecución con Docker

Construir la imagen:

```bash
docker compose build
```

Ejecutar la aplicación principal:

```bash
docker compose run --rm turismo-cartago
```

Ejecutar la preparación de datos:

```bash
docker compose run --rm turismo-cartago python src/preparacion_datos.py
```

Ejecutar el perceptrón:

```bash
docker compose run --rm turismo-cartago python src/perceptron_proyecto.py
```

Para abrir una terminal interactiva dentro del contenedor:

```bash
docker compose run --rm --entrypoint bash turismo-cartago
```

Ya dentro del contenedor:

```bash
cd /app/src
python perceptron_proyecto.py
```

Detener los servicios activos:

```bash
docker compose down
```

Los archivos generados se guardan en la carpeta local `graficos` si el volumen está configurado para compartir esos archivos con el equipo.
