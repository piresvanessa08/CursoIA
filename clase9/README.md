# Clase 9: perceptrón completo

Proyecto de la actividad grupal de Inteligencia Artificial. El modelo estima la probabilidad de éxito de cosecha usando precipitación y temperatura. El conjunto de 120 lotes es simulado por el material del curso.

## Archivos

- `src/generar_datos.py`: genera `data/cultivos_cartago.csv` con semilla fija.
- `src/neurona_clase8.py`: ejecuta el diagnóstico de la neurona anterior.
- `src/perceptron_reto.py`: solución de los siete retos.
- `Informe_Clase9_Tatiana_Vanessa_Alvis.pdf`: informe con resultados y gráficas.
- `requirements.txt`: dependencias de Python.

## Abrir en Visual Studio Code

Abre la carpeta `clase9` desde VS Code. Para ejecutar los scripts, abre una terminal integrada y usa:

```powershell
cd src
python -m pip install -r ../requirements.txt
python generar_datos.py
python neurona_clase8.py
python perceptron_reto.py
```

Ejecuta los comandos desde `src`, porque los scripts usan rutas relativas al directorio de datos. También se pueden ejecutar dentro del contenedor Docker preparado para las clases.

`perceptron_reto.py` crea `curva_aprendizaje.png` y `frontera_decision.png` en el directorio actual. Las etiquetas del dataset son simuladas para fines pedagógicos y no deben tomarse como recomendaciones agrícolas reales.

## Nota del informe

El informe identifica el trabajo como individual y deja editables el número de grupo, la fecha de entrega y la hipótesis previa, que deben completarse según lo registrado y solicitado por el docente.
