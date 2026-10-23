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
│   ├── perceptron_proyecto.py
│   ├── preparacion_datos.py
│   └── recomendador.py
└── tests/
    └── test_perceptron_proyecto.py
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

Los archivos generados son `data/datos_turisticos_limpios.csv` y
`data/sitios_turisticos_preparados_ml.csv`. Las visualizaciones de Seaborn se
guardan en `graficos/`: distribución de visitantes, promedio de visitantes
por categoría, relación entre visitantes y calificación, y relación entre las
entradas del perceptrón y su objetivo. El gráfico existente
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

## Avance 2

La preparación y el perceptrón son actividades independientes: no cambian el
CSV original, el menú ni el recomendador. Para generar los datos limpios, los
tres gráficos de Seaborn y el CSV codificado:

```powershell
python src\preparacion_datos.py
```

### Objetivo y entradas del perceptrón

El script `src/perceptron_proyecto.py` entrena desde cero con NumPy un modelo
logístico de dos entradas. Para esta demostración académica, la clase positiva
se define como `visitantes_mes >= mediana`; la mediana de los siete registros
actuales es 3.200 visitantes mensuales. `visitantes_mes` define la etiqueta y
por eso no se usa como entrada. Las entradas son `calificacion` y
`es_gratuito`, estandarizadas con la media y desviación estándar del conjunto.
El script implementa la sigmoide, la pérdida logarítmica y el descenso del
gradiente sin usar Scikit-Learn.

### Ajustes, tabla y análisis visual

No se recibieron observaciones específicas sobre la sustentación del Avance 1;
por tanto, no se atribuyen cambios a comentarios inexistentes. Este avance
documenta por separado el trabajo de preparación de datos, visualización y
modelo solicitado en la guía.

En el CSV fuente hay 7 filas, 6 columnas, 0 nulos y 0 duplicados. La limpieza
no elimina ni imputa registros porque no se encontraron problemas en esos
datos. El archivo limpio añade el indicador derivado `es_gratuito`; la tabla
codificada para explorar ML agrega las columnas One-Hot de categoría.

| Etapa | Filas | Columnas | Nulos | Duplicados |
|---|---:|---:|---:|---:|
| CSV original | 7 | 6 | 0 | 0 |
| CSV limpio, con `es_gratuito` | 7 | 7 | 0 | 0 |
| CSV preparado, con categorías codificadas | 7 | 9 | 0 | 0 |

La autora indicó que la información turística se consultó en las fuentes de la
sección **Referencias**. La relación exacta entre cada valor del CSV
(visitantes por sitio, calificaciones y precios) y una tabla o página concreta
de esas fuentes aún debe cotejarse antes de presentar cada valor como una
transcripción directa. La publicación de Facebook se conserva solo como
referencia complementaria, no como fuente estadística primaria.

Interpretación de los gráficos de Seaborn:

1. **Distribución de visitantes:** muestra registros entre 1.200 y 5.000
   visitantes mensuales. La muestra es pequeña y el histograma describe estos
   siete sitios, no la demanda turística completa.
2. **Visitantes promedio por categoría:** Compras tiene 5.000 visitantes y
   Recreativo promedia 3.000 entre sus dos sitios. Las demás categorías tienen
   un solo registro, por lo que las diferencias no son generalizables.
3. **Visitantes y calificación:** Casa del Virrey combina la menor afluencia
   (1.200) con una calificación de 4,9; el centro comercial combina la mayor
   afluencia (5.000) con 4,3. Esto no prueba una relación causal o predictiva.
4. **Entradas y objetivo:** `seaborn_entradas_objetivo.png` compara la
   calificación y el acceso gratuito entre las clases menor y mayor que la
   mediana de visitantes (3.200). Permite inspeccionar las entradas utilizadas
   por el perceptrón; siete registros no bastan para establecer una regla
   predictiva confiable.

Ejecución local desde `TurismoCartagoIA`:

```powershell
python src\perceptron_proyecto.py
```

El programa informa los dos pesos, el sesgo, las pérdidas inicial y final y la
exactitud sobre los mismos siete registros usados para entrenar. También
genera `graficos/perceptron_curva_aprendizaje.png` y
`graficos/perceptron_frontera_decision.png`.

En la ejecución de referencia, la pérdida baja de 0,693147 a 0,287596 y la
exactitud de entrenamiento es 85,71 %. Ambos pesos son positivos en esta
ejecución: dentro de este ajuste, una calificación estandarizada mayor y el
acceso gratuito se asocian con una probabilidad estimada mayor de pertenecer a
la clase de alta afluencia. Esto no demuestra causalidad. La frontera lineal
no separa perfectamente los registros: queda al menos un error de
clasificación en la ejecución de referencia.

**Limitación:** siete observaciones no permiten una evaluación independiente ni
conclusiones generalizables. La exactitud informada es de entrenamiento; se
presenta solo para demostrar el algoritmo solicitado, no como rendimiento
predictivo validado. Los datos de entrada del proyecto no incluyen una
referencia trazable por fila para los valores de visitantes, calificaciones y
precios; la verificación de la tabla/página de origen y el período de cada
métrica queda pendiente antes de presentar resultados como evidencia real.

Los gráficos y archivos de datos se generan a partir del CSV fuente; el script
del perceptrón no cambia ese archivo.

### Plan hacia el proyecto final

El problema de esta demostración es de **clasificación binaria**: distinguir
entre afluencia menor a la mediana y afluencia igual o mayor a la mediana. Para
la comparación de la Clase 12 se propone evaluar regresión logística y árbol
de decisión con *balanced accuracy*, para considerar el desempeño de ambas
clases. Antes de comparar modelos formalmente, se deben ampliar y documentar
los datos; siete registros no permiten una partición de prueba ni una
validación cruzada que respalde conclusiones. El calendario y los casos nuevos
de demostración se completarán en el documento de entrega cuando se confirmen
con el grupo.

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

Ejecutar el perceptrón dentro del contenedor:

```powershell
docker compose run --rm turismo-cartago python src/perceptron_proyecto.py
```

Para abrir una terminal interactiva en el contenedor y mostrar el prompt
solicitado durante el video:

```powershell
docker compose run --rm --entrypoint bash turismo-cartago
```

Ya dentro del contenedor:

```bash
cd /app/src
python perceptron_proyecto.py
```

Detener servicios activos:

```powershell
docker compose down
```

La gráfica se guarda en la carpeta `graficos` del proyecto porque Docker monta
la carpeta local como volumen.

## Referencias

Fuentes compartidas por la autora del proyecto; consultadas el 22 de octubre de
2026:

1. SITUR Valle. (s. f.). *Estadísticas*. https://siturvalle.com/estadisticas/
2. Municipio de Cartago. (2022). *Anuario Estadístico – Cartago 2022*.
   https://cartago.gov.co/anuario-estadistico-cartago-2022/
3. Publicación de Facebook sobre visitantes alojados en Cartago durante Semana
   Santa. (s. f.). Referencia complementaria; no se usa como fuente primaria
   para entrenar o validar el modelo.
   https://www.facebook.com/100007741248027/photos/cartago-la-ciudad-del-valle-que-m%C3%A1s-turistas-aloj%C3%B3-en-la-semana-santa-seg%C3%BAn-dato/2931266880474658/

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

## Guion sugerido para el video

Para cumplir el criterio más estricto de duración indicado en la guía, preparar
una grabación de hasta 5 minutos:

1. **0:00–0:40:** presentarse como Tatiana Vanessa Alvis, nombrar el proyecto y
   explicar el problema turístico que se busca abordar.
2. **0:40–1:30:** mostrar el CSV, sus siete filas, cero nulos y cero duplicados;
   explicar la tabla antes/después y las decisiones de limpieza.
3. **1:30–2:15:** mostrar los cuatro gráficos de Seaborn y resumir un hallazgo,
   aclarando que son solo siete registros.
4. **2:15–4:15:** mostrar el terminal Docker. Ejecutar
   `docker compose run --rm --entrypoint bash turismo-cartago`, entrar a
   `/app/src`, ejecutar `python perceptron_proyecto.py` y explicar el umbral,
   las entradas, la pérdida, los pesos y los gráficos. Aclarar que el 85,71 %
   es exactitud sobre entrenamiento, no validación independiente.
5. **4:15–5:00:** presentar la propuesta de comparar regresión logística y
   árbol de decisión con *balanced accuracy*, condicionada a conseguir más
   datos trazables; cerrar indicando los próximos pasos.

Antes de entregar, grabar y subir el video, pegar aquí o en AVACO su enlace
público, y probarlo en una ventana de incógnito. La guía menciona tanto 10 como
5 minutos; esta propuesta respeta el máximo de 5 minutos que aparece en la
rúbrica.
