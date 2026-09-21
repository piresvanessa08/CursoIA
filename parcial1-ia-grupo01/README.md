# Parcial 1 - Inteligencia Artificial - Grupo 01

## 1. Descripcion del proyecto

Este proyecto corresponde al Parcial 1 de la asignatura Inteligencia Artificial.

El objetivo es cargar, limpiar, analizar e interpretar datos reales relacionados con fincas cafeteras de la region de Cartago.

El analisis se realiza utilizando Python, NumPy y Matplotlib, y el proyecto se ejecuta tambien mediante Docker.

El archivo de datos asignado al Grupo 01 es:

`grupo_01.txt`

---

## 2. Tecnologias utilizadas

- Python 3.12
- NumPy
- Matplotlib
- Docker
- Docker Compose
- Git y GitHub
- Visual Studio Code

---

## 3. Estructura del proyecto

parcial1-ia-grupo01
|-- analisis.py
|-- grupo_01.txt
|-- Dockerfile
|-- docker-compose.yml
|-- requirements.txt
|-- README.md
`-- graficos
    |-- distribucion_produccion.png
    `-- hectareas_vs_produccion.png

---

## 4. Configuracion del entorno

El proyecto utiliza Python 3.12 mediante Docker.

Las principales dependencias se encuentran en el archivo `requirements.txt`.

Contenido:

    numpy
    matplotlib

El archivo `Dockerfile` utiliza la imagen oficial de Python 3.12 y realiza la instalacion de las dependencias necesarias.

El archivo `docker-compose.yml` permite construir y ejecutar el proyecto mediante Docker Compose.

---

## 5. Carga de datos

El archivo `analisis.py` utiliza `csv.DictReader` para leer el archivo `grupo_01.txt`.

El programa:

1. Carga los datos.
2. Muestra los primeros 5 registros.
3. Muestra el numero total de registros.
4. Convierte las variables numericas en arreglos de NumPy.
5. Realiza el analisis estadistico.
6. Identifica problemas de calidad.
7. Genera graficos.
8. Calcula la correlacion entre hectareas y produccion.
9. Presenta una interpretacion de los resultados.
10. Genera una recomendacion basada en los datos.

---

## 6. Analisis de calidad de los datos

Se encontraron varios problemas importantes en el conjunto de datos.

### Problema 1: Dato faltante

El registro correspondiente a la finca `El Roble` no contiene un valor para `produccion_kg`.

Deteccion:

Se identifico el campo vacio durante la lectura del archivo CSV.

Decision:

El valor faltante no se reemplaza por un valor inventado. Para los calculos estadisticos de produccion se utilizan solamente los registros que tienen un valor disponible.

Justificacion:

Asignar un valor sin informacion adicional podria alterar los resultados del analisis.

---

### Problema 2: Valor atipico

La finca `La Montana` presenta una produccion de:

`51000 kg`

La mayoria de los valores de produccion se encuentran aproximadamente entre `1200 kg` y `5800 kg`.

Deteccion:

El valor 51000 kg se identifica como sospechoso porque es considerablemente mayor que el resto de los registros.

Decision:

El valor no se elimina automaticamente. Se conserva para identificarlo como posible valor atipico y se realiza una comparacion adicional excluyendolo.

Justificacion:

El dato podria ser un error de digitacion o podria representar una situacion agricola real. Por lo tanto, debe ser validado antes de eliminarlo.

---

### Problema 3: Identificacion repetida de una finca

La finca `La Esperanza` aparece en dos registros.

Los registros no son completamente iguales porque presentan diferentes valores de hectareas y produccion.

Decision:

No se eliminan automaticamente los registros.

Se recomienda verificar si se trata de la misma finca registrada dos veces o si corresponde a diferentes periodos o unidades de produccion.

Justificacion:

Eliminar uno de los registros sin verificar su significado podria provocar perdida de informacion.

---

## 7. Valor sospechoso

El valor que genera mayor sospecha es:

`La Montana = 51000 kg`

Este valor es muy superior a la mayoria de los datos del conjunto.

Su presencia afecta considerablemente el promedio de produccion.

Por esta razon se recomienda verificar este registro antes de utilizarlo para tomar decisiones.

---

## 8. Estadisticas de produccion

Para la variable `produccion_kg` se tienen 12 registros con datos disponibles.

Resultados:

- Media: 7041.67 kg
- Mediana: 2950 kg
- Desviacion estandar: 13305.60 kg
- Minimo: 1200 kg
- Maximo: 51000 kg

La media es mucho mayor que la mediana.

Esto ocurre principalmente por la presencia del valor atipico de 51000 kg.

La mediana de 2950 kg representa mejor una produccion tipica del conjunto de datos.

---

## 9. Comparacion sin el valor atipico

Al excluir temporalmente el valor de 51000 kg para observar su efecto:

- Media: 3045.45 kg
- Mediana: 2800 kg
- Desviacion estandar: 1223.53 kg

La diferencia demuestra que el valor de 51000 kg tiene una influencia muy fuerte sobre las estadisticas.

Por esta razon, la mediana resulta mas representativa para describir una produccion tipica.

---

## 10. Analisis de hectareas

Para la variable `hectareas` se obtuvieron los siguientes resultados:

- Media: 5.08 hectareas
- Mediana: 5 hectareas
- Desviacion estandar: 1.98 hectareas
- Minimo: 2 hectareas
- Maximo: 9 hectareas

Los datos muestran que las fincas analizadas tienen diferentes tamaños, entre 2 y 9 hectareas.

---

## 11. Analisis de altitud

Para la variable `altitud_msnm`:

- Media: 1650.77 metros
- Mediana: 1650 metros
- Desviacion estandar: 68.89 metros
- Minimo: 1520 metros
- Maximo: 1750 metros

La altitud presenta una variacion menor que la produccion.

---

## 12. Visualizaciones

El proyecto genera dos graficos utilizando Matplotlib.

### Grafico 1: Distribucion de la produccion

Archivo:

`graficos/distribucion_produccion.png`

Este grafico permite observar como se distribuyen los valores de produccion.

La distribucion esta fuertemente afectada por el valor de 51000 kg, que se encuentra muy alejado de los demas registros.

Esto confirma visualmente la presencia de un posible valor atipico.

---

### Grafico 2: Hectareas frente a produccion

Archivo:

`graficos/hectareas_vs_produccion.png`

Este grafico relaciona el numero de hectareas de cada finca con su produccion.

En general se observa una tendencia positiva: las fincas con mayor cantidad de hectareas tienden a presentar mayores producciones.

Sin embargo, la relacion no es perfecta.

---

## 13. Correlacion

Se calculo la correlacion entre las hectareas y la produccion.

Resultado:

`r = 0.52`

Este resultado representa una relacion positiva y moderada entre ambas variables.

En general, al aumentar las hectareas tambien tiende a aumentar la produccion.

Sin embargo, una correlacion no demuestra causalidad.

No se puede afirmar solamente con estos datos que aumentar las hectareas sea la causa directa de una mayor produccion.

Tambien pueden influir otros factores como:

- Variedad de cafe.
- Altitud.
- Clima.
- Suelo.
- Manejo de la finca.
- Productividad por hectarea.

---

## 14. Interpretacion profunda

Los datos permiten observar varias situaciones importantes.

Primero, la produccion presenta una gran variacion.

El valor de 51000 kg cambia considerablemente el comportamiento de las estadisticas.

La media de 7041.67 kg es mucho mayor que la mediana de 2950 kg.

Esto indica que la media no representa adecuadamente una produccion tipica cuando se considera todo el conjunto.

Cuando se excluye temporalmente el valor atipico, la media disminuye hasta 3045.45 kg.

Esto demuestra la influencia que tiene el valor de 51000 kg.

Tambien se observa una relacion positiva entre las hectareas y la produccion, con una correlacion de 0.52.

Sin embargo, esta relacion no permite afirmar causalidad.

Para comprender mejor las diferencias de produccion seria necesario contar con informacion adicional sobre las condiciones de cada finca.

---

## 15. Historia de los datos en el contexto de Cartago

Los datos representan diferentes fincas cafeteras con variaciones en tamaño, altitud, variedad y produccion.

Las fincas tienen entre 2 y 9 hectareas y se encuentran entre 1520 y 1750 metros sobre el nivel del mar.

La produccion presenta diferencias importantes entre las fincas.

La mayor diferencia corresponde al registro de La Montana, que reporta 51000 kg.

Esta diferencia podria representar una situacion agricola particular o un problema de calidad de datos.

Por esta razon, el analisis permite identificar situaciones que deberian ser verificadas antes de tomar decisiones.

---

## 16. Recomendacion

Se recomienda validar la informacion antes de utilizar estos datos para tomar decisiones agricolas.

Las principales acciones recomendadas son:

1. Verificar el registro de La Montana y confirmar si la produccion de 51000 kg es correcta.
2. Completar el dato faltante de produccion de El Roble.
3. Verificar por que La Esperanza aparece en dos registros.
4. Mantener un control de calidad de los datos antes de realizar nuevos analisis.
5. Registrar informacion adicional sobre clima, suelo y manejo agricola.

Esta recomendacion se fundamenta en varios resultados concretos:

- La produccion maxima es de 51000 kg.
- La produccion mediana es de 2950 kg.
- La media es de 7041.67 kg.
- Existe un dato faltante.
- La correlacion entre hectareas y produccion es de 0.52.

Estos resultados muestran que es necesario validar la informacion y contar con mayor contexto antes de realizar conclusiones agricolas definitivas.

---

## 17. Limitaciones del analisis

El conjunto de datos presenta algunas limitaciones.

La primera es que solamente existen 13 registros.

Ademas, existe un dato faltante en produccion.

Tambien existe un valor de produccion muy alejado del resto de los registros.

No se cuenta con suficiente informacion sobre factores que pueden afectar la produccion.

Por ejemplo:

- Condiciones climaticas.
- Caracteristicas del suelo.
- Tipo de fertilizacion.
- Manejo de los cultivos.
- Edad de los cultivos.
- Productividad por hectarea.
- Plagas o enfermedades.
- Periodo exacto de produccion.

Por estas razones, los resultados deben interpretarse como un analisis exploratorio y no como una prueba definitiva de las causas de la produccion.

---

## 18. Datos adicionales recomendados

Para mejorar el analisis seria conveniente recolectar:

- Produccion por hectarea.
- Fecha o periodo de cosecha.
- Variedad del cafe.
- Condiciones climaticas.
- Precipitacion.
- Temperatura.
- Tipo de suelo.
- Uso de fertilizantes.
- Edad de los cultivos.
- Sistemas de riego.
- Presencia de plagas o enfermedades.
- Metodos de manejo agricola.

Con estos datos seria posible realizar un analisis mas completo y obtener mejores conclusiones.

---

## 19. Ejecucion local

Para ejecutar el proyecto directamente con Python:

    python analisis.py

El programa mostrara los resultados en la terminal y generara los graficos dentro de la carpeta `graficos`.

---

## 20. Ejecucion con Docker

Para construir la imagen:

    docker compose build

Para ejecutar el analisis:

    docker compose run --rm parcial

Docker permite reproducir el entorno utilizando Python 3.12 y las dependencias definidas en `requirements.txt`.

---

## 21. Archivos entregados

El repositorio contiene:

- `analisis.py`
- `grupo_01.txt`
- `Dockerfile`
- `docker-compose.yml`
- `requirements.txt`
- `README.md`
- `graficos/distribucion_produccion.png`
- `graficos/hectareas_vs_produccion.png`

---

## 22. Conclusiones

El analisis exploratorio permitio identificar problemas de calidad en los datos y obtener informacion relevante sobre la produccion de las fincas.

El principal hallazgo es el valor de 51000 kg correspondiente a La Montana, ya que afecta considerablemente la media.

La mediana de 2950 kg representa mejor una produccion tipica del conjunto.

Tambien se encontro una relacion positiva moderada entre hectareas y produccion, con una correlacion de 0.52.

Sin embargo, esta relacion no demuestra causalidad.

Antes de tomar decisiones agricolas se recomienda validar los datos y recolectar informacion adicional que permita explicar mejor las diferencias observadas.

---

## 23. Autor

Parcial 1 - Inteligencia Artificial

Grupo 01