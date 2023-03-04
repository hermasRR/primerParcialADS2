# Usar la imagen de Python como base
FROM python:3.8

# Establecer la ruta de trabajo dentro del contenedor
WORKDIR /app
# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt .
# Crear y activar un entorno virtual
RUN python3 -m venv venv
RUN . venv/bin/activate 
RUN pip install -r requirements.txt
# Copiar el código de la aplicación al contenedor
COPY . .

# Establecer la variable de entorno FLASK_APP
ENV FLASK_APP=app.py
# Establecer la variable de entorno FLASK_ENV
ENV FLASK_ENV=development
# Establecer la variable de entorno FLASK_DEBUG
ENV FLASK_DEBUG=1

# Exponer el puerto 5000
EXPOSE 5000

# Ejecutar la aplicación Flask
CMD ["flask", "run", "--host=0.0.0.0"]


