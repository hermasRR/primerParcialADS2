#!/bin/bash

sudo chmod +x run.sh
# Iniciar Nginx en segundo plano
nginx -g "daemon off;" &

# Ejecutar la aplicación Python en primer plano
python3 app.py

# Ejecutar las pruebas de testing
#pytest -v
#docker exec -it test_server pytest -v