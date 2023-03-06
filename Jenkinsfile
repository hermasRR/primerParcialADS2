pipeline {
    agent any
    
    stages {
        stage('Clonar código fuente') {
            steps {
                git 'https://github.com/hermasRR/primerParcialADS2.git'
            }
        }
        stage('Instalar dependencias') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Ejecutar pruebas') {
            steps {
                sh 'pytest -v'
            }
        }
        stage('Construir imagen de Docker') {
            steps {
                sh 'docker build --no-cache -t examenParcial .'
            }
        }
    }
}
