FROM python:3.12-slim

WORKDIR /app

# 1. Crear el entorno virtual en una ruta limpia
RUN python -m venv /opt/venv

# 2. Usar el entorno virtual como predeterminado
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .

# 3. Instalar las dependencias dentro del entorno virtual
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

CMD ["python", "src/main.py"]