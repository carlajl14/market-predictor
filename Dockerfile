FROM python:3.11-slim

# Establecer el directorio de trabajo
WORKDIR /

# Copiar el archivo requirements.txt
COPY requirements.txt .

# Instalar dependencias del sistema necesarias para TensorFlow y otras bibliotecas
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    libpq-dev \
    gcc \
    liblapack-dev \
    gfortran \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libgomp1 \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Actualizar pip a la última versión
RUN pip install --upgrade pip

# Instalar dependencias de Python desde requirements.txt con la opción --verbose para depuración
RUN pip install --no-cache-dir -r requirements.txt --verbose

# Copiar el resto de los archivos del proyecto al contenedor
COPY . .

# Exponer el puerto 8080
EXPOSE 8080

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]