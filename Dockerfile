FROM ubuntu:latest

# Actualizar los paquetes y herramientas de Ubuntu
RUN apt-get update && apt-get install -y git python3-pip nginx wget xvfb unzip gnupg
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update && apt-get install -y google-chrome-stable

# Clonar el repositorio 
RUN git clone https://github.com/hermasRR/primerParcialADS2.git

# Establece el directorio de trabajo en la carpeta de la aplicación
WORKDIR /primerParcialADS2

# Copia la aplicación a la carpeta de nginx
COPY . /var/www/html

RUN pip3 install flask pytest pytest-html selenium mysql-connector mysql-connector-python

# Configura el servidor virtual de nginx
RUN rm /etc/nginx/sites-enabled/default
COPY default /etc/nginx/sites-enabled/

# Exponer el puerto 4001, utilizado por nginx
EXPOSE 8000

# Copiar el script de inicialización
COPY run.sh /usr/local/bin/

# Establecer el script de inicialización como comando a ejecutar
CMD ["bash", "/usr/local/bin/run.sh"]


