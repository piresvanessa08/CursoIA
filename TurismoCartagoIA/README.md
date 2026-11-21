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
├── docs/
│   └── Informe_Final_TurismoCartagoIA.pdf
├── data/
│   ├── sitios_turisticos_cartago.csv
│   ├── datos_turisticos_limpios.csv
│   ├── sitios_turisticos_preparados_ml.csv
│   ├── base_visitantes_municipal_2025.csv
│   └── comparacion_modelos.csv
├── models/
│   └── modelo_turismo.joblib
├── graficos/
│   ├── visitantes_sitios.png
│   ├── seaborn_distribucion_visitantes.png
│   ├── seaborn_visitantes_categoria.png
│   ├── seaborn_visitantes_calificacion.png
│   ├── perceptron_curva_aprendizaje.png
│   └── matriz_confusion_modelo.png
├── src/
│   ├── cargar_datos.py
│   ├── eda_proyecto.py
│   ├── main.py
│   ├── perceptron_proyecto.py
│   ├── preparacion_datos.py
│   ├── recomendador.py
│   ├── modelo_proyecto.py
│   └── usar_modelo.py
└── tests/
    └── test_perceptron_proyecto.py
```

## Datos

El archivo `data/sitios_turisticos_cartago.csv` contiene 33 atractivos. Se incorporaron 23 atractivos del listado suministrado por la usuaria, asignados a las categorías existentes; los que ya estaban registrados se conservaron sin duplicarlos. El Aeropuerto de Santa Ana no se incluyó. Los visitantes por atractivo son estimaciones para el prototipo y todas las filas llevan `datos_estimados=1`; los datos de calificación, precio y horario de los 26 registros incorporados también son aproximados y no están verificados.

El documento municipal de flujo turístico de Cartago para 2025 registra 196.568 visitantes en el año, pero no desglosa cifras por atractivo. Para construir una base comparable, el proyecto calcula un promedio mensual de 16.381 (196.568 / 12, redondeado) y lo distribuye entre los 33 sitios, conservando las proporciones relativas de las estimaciones previas y normalizándolas a 100 %. La columna `participacion_estimada_pct` deja visibles los pesos. El redondeo por mayor residuo mantiene la suma mensual en 16.381.

Entre los registros se encuentra Restaurante Casa Vieja, de categoría Gastronomía, con horario de 12:00 m. a 9:00 p. m.

### Base municipal y distribución por sitio

El archivo `data/base_visitantes_municipal_2025.csv` conserva el total anual de referencia y el promedio mensual calculado. El CSV de sitios distribuye el promedio mensual según las participaciones registradas en `participacion_estimada_pct`; las cifras por atractivo se deben interpretar como estimaciones y los modelos derivados como demostrativos.

## Análisis y gráfica

El programa calcula el total de sitios, el promedio, el máximo, el mínimo y la desviación estándar de visitantes, además del promedio general de calificaciones.

La gráfica se guarda en:

`graficos/visitantes_sitios.png`

La gráfica utiliza barras horizontales ordenadas de mayor a menor, colores por categoría y nombres completos. El número aparece al final de cada barra y las etiquetas `[Gratis]` identifican los sitios con precio de entrada igual a cero.

## Preparación de datos

La actividad independiente de Pandas y Seaborn se aplica al conjunto de datos turísticos del proyecto. Se ejecuta por separado; no cambia el menú de recomendaciones ni modifica el CSV de entrada.

```bash
python src/preparacion_datos.py
```

La actividad aplica al conjunto de datos turístico las operaciones de la guía: selección de columnas relevantes, filtrado de sitios con afluencia igual o superior a la mediana, ordenamiento por visitantes y agrupación por categoría. El resumen de categorías calcula la cantidad de sitios, los visitantes totales, el promedio de visitantes y la calificación promedio a partir del CSV.

El análisis lee `data/sitios_turisticos_cartago.csv` con Pandas e informa las primeras y últimas filas, dimensiones, tipos de datos, estadísticas, valores nulos y duplicados.

El CSV fuente tiene 33 filas y diez columnas. Los 33 valores de visitantes son estimaciones; los 26 registros incorporados también contienen aproximaciones de calificación, precio y horario. Los valores no se deben presentar como observaciones reales.

Si aparecen valores nulos en otros datos, el script utiliza la mediana para columnas numéricas y la moda para las categóricas. Para nombres u horarios ausentes utiliza `No especificado`, sin atribuir a un sitio la identidad u horario de otro. Las filas exactamente duplicadas se excluyen del archivo limpio.

Se genera `es_gratuito` a partir de `precio` para identificar lugares con entrada gratuita. Para el archivo de preparación se codifica `categoria` mediante One-Hot Encoding. Se conservan `visitantes_mes` y `calificacion` como columnas numéricas. `precio` no se duplica como característica porque se utiliza el indicador `es_gratuito` para distinguir el acceso gratuito.

Los archivos generados son:

- `data/datos_turisticos_limpios.csv`
- `data/sitios_turisticos_preparados_ml.csv`

Las visualizaciones de Seaborn se guardan en `graficos/`: distribución de visitantes, promedio de visitantes por categoría, relación entre visitantes y calificación, y relación entre las entradas del perceptrón y su objetivo. La gráfica `graficos/visitantes_sitios.png` se genera con barras horizontales para facilitar la lectura de los 33 nombres.

En los 33 registros, la distribución estimada suma 16.381 visitantes mensuales, con un promedio de aproximadamente 496 por atractivo.

La cantidad de sitios por categoría refleja la selección del prototipo, no la oferta total de Cartago. Los promedios y comparaciones por categoría son ilustrativos y no permiten conclusiones sobre la afluencia real.

El resumen agrupado permite distinguir entre afluencia total y promedio. Los valores por categoría reflejan la distribución del conjunto y el tamaño pequeño de la muestra. La gráfica de dispersión de visitantes y calificación sirve para explorar los registros, pero no basta para concluir que una variable causa o predice la otra.

## Avance 2

La preparación de datos y el perceptrón son actividades independientes: no cambian el CSV original, el menú ni el recomendador.

Para generar los datos limpios, los gráficos de Seaborn y el CSV codificado:

```bash
python src/preparacion_datos.py
```

### Objetivo y entradas del perceptrón

El script `src/perceptron_proyecto.py` entrena desde cero, utilizando NumPy, un modelo logístico de dos entradas.

Para esta demostración académica, la clase positiva se define como `visitantes_mes >= mediana`. El umbral se calcula sobre los 33 registros estimados; en la distribución actual es de 368 visitantes mensuales. `visitantes_mes` define la etiqueta y, por eso, no se utiliza como entrada.

Las entradas son `calificacion` y `es_gratuito`, estandarizadas con la media y la desviación estándar del conjunto. El script implementa el sigmoide, la pérdida logarítmica y el descenso del gradiente sin utilizar Scikit-Learn.

### Ajustes, tabla y análisis visual

No se recibieron observaciones específicas sobre la sustentación del Avance 1; por tanto, no se atribuyen cambios a comentarios inexistentes. Este avance documenta por separado el trabajo de preparación de datos, visualización y modelo solicitado en la guía.

El CSV original tiene 33 filas y diez columnas. Los visitantes de los 33 registros son estimaciones distribuidas con pesos relativos; las calificaciones, precios y horarios de los 26 atractivos incorporados también son aproximados. La tabla codificada incluye los 33 registros, por lo que sus métricas son demostrativas.

| Etapa | Filas | Columnas | Nulos | Duplicados |
|---|---:|---:|---:|---:|
| CSV original | 33 | 10 | 7 | 0 |
| CSV limpio, con `es_gratuito` | 33 | 11 | 7 | 0 |
| CSV preparado, con categorías codificadas | 33 | 9 | 0 | 0 |

El CSV preparado tiene nueve columnas: tres características numéricas y seis columnas binarias para las categorías. Las siete celdas vacías en las dos primeras etapas corresponden a sitios sin una fuente documentada para sus datos descriptivos; las participaciones están completas para los 33 atractivos.

La referencia municipal es agregada y no reporta afluencia por atractivo. La distribución por sitio es una aproximación reproducible a partir del promedio mensual y de los pesos publicados en el CSV; no debe citarse como medición individual. Las calificaciones, precios y horarios también requieren verificación independiente.

### Interpretación de los gráficos de Seaborn

- **Distribución de visitantes:** muestra valores entre 123 y 1.712 visitantes mensuales por sitio.
- **Visitantes promedio por categoría:** los promedios reflejan la distribución del total municipal y no permiten comparar la afluencia real de las categorías.
- **Visitantes y calificación:** la relación se explora con valores de visitantes prorrateados y calificaciones preexistentes; no prueba causalidad ni capacidad predictiva.
- **Entradas y objetivo:** `seaborn_entradas_objetivo.png` compara la calificación y el acceso gratuito entre las clases definidas por la mediana de visitantes. Los 33 registros estimados no permiten establecer una regla predictiva confiable.

### Ejecución local del perceptrón

Desde la carpeta `TurismoCartagoIA`:

```bash
python src/perceptron_proyecto.py
```

El programa informa los dos pesos, el sesgo, las pérdidas inicial y final y la exactitud sobre los mismos 33 registros utilizados para entrenar. También genera:

- `graficos/perceptron_curva_aprendizaje.png`
- `graficos/perceptron_frontera_decision.png`

En la ejecución actual, la pérdida baja de 0,693147 a 0,550726 y la exactitud sobre los mismos 33 registros de entrenamiento es de 66,67 %. Los pesos de calificación y gratuidad son positivos en este ajuste. Con un conjunto pequeño que incluye estimaciones, esos signos describen la solución matemática de esta corrida; no son evidencia de que la calificación o el acceso gratuito aumenten la afluencia real.

La frontera lineal no separa perfectamente los registros de entrenamiento.

**Limitación:** las 33 observaciones contienen cifras estimadas distribuidas a partir de un total municipal agregado y no permiten conclusiones generalizables. La exactitud informada es de entrenamiento; se presenta solo para demostrar el algoritmo solicitado, no como rendimiento predictivo validado. Las calificaciones, precios y horarios requieren verificación independiente.

Los gráficos y archivos de datos se generan a partir de la fuente CSV; el script del perceptrón no cambia ese archivo.

## Resultados del modelo de clasificación

La última ejecución seleccionó la regresión logística con F1 medio de validación cruzada de 0,843. En la prueba de siete filas obtuvo exactitud 0,857, precisión 0,800, recall 1,000 y F1 0,889. Son métricas demostrativas del conjunto de datos del proyecto; no representan rendimiento turístico validado.

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

Fuentes consultadas el 15 de noviembre de 2026:

- Reporte municipal de flujo turístico de Cartago (2025), documento PDF facilitado para el proyecto.
- Municipio de Cartago. (2022). *Anuario Estadístico – Cartago 2022*. https://cartago.gov.co/anuario-estadistico-cartago-2022/
- Concejo Municipal de Cartago. (2022). *Plan Sectorial de Turismo 2022–2032*. https://www.cartago.gov.co/Docs/ACUERDO%20No.%20017-2022-ADOPTA%20PLAN%20SECTORIAL%20DE%20TURISMO.pdf
- Scikit-learn developers. (s. f.). *Cross-validation: Evaluating estimator performance*. https://scikit-learn.org/stable/modules/cross_validation.html
- Scikit-learn developers. (s. f.). *Pipeline*. https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html
- Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., Vanderplas, J., Passos, A., Cournapeau, D., Brucher, M., Perrot, M., & Duchesnay, É. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research, 12*, 2825–2830. https://www.jmlr.org/papers/v12/pedregosa11a.html
- Harris, C. R., Millman, K. J., van der Walt, S. J., et al. (2020). Array programming with NumPy. *Nature, 585*(7825), 357–362. https://doi.org/10.1038/s41586-020-2649-2
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

## Modelo de clasificación de Clase 12

El script `src/modelo_proyecto.py` compara regresión logística, KNN y árbol de decisión para clasificar afluencia alta (visitantes mensuales iguales o superiores a la mediana) frente a afluencia menor. Usa los 33 registros, todos con visitantes estimados.

Cada modelo utiliza un `Pipeline` que escala las variables numéricas y codifica la categoría. Los datos se separan con `test_size=0.2`, `random_state=42` y estratificación. La selección se hace por F1 promedio de validación cruzada sobre entrenamiento; se informa exactitud, precisión, recall y F1 en prueba, se guarda la matriz de confusión y se serializa el mejor Pipeline junto con sus metadatos.

Desde la raíz `TurismoCartagoIA`, ejecuta primero el entrenamiento y luego la demostración:

```bash
python src/modelo_proyecto.py
python src/usar_modelo.py
```

El modelo queda en `models/modelo_turismo.joblib`; la tabla de métricas, en `data/comparacion_modelos.csv`; y la matriz de confusión, en `graficos/matriz_confusion_modelo.png`. Los valores de visitantes por sitio son estimaciones; las calificaciones, precios y horarios requieren confirmación. Las métricas son demostrativas y no representan rendimiento turístico validado en población.

## Entregables del proyecto final

- Informe final en PDF: `docs/Informe_Final_TurismoCartagoIA.pdf`.
- Repositorio: https://github.com/piresvanessa08/CursoIA/tree/main/TurismoCartagoIA

Antes de entregar, verifica que el repositorio público incluya los últimos cambios y que el enlace funcione desde una ventana privada.
