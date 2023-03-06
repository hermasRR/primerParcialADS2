pipeline {
    agent {
        docker {
            image 'server-testing1:latest'
            args '-p 4001:4001'
        }
    }
    stages {
        stage('Ejecutar contenedor') {
            steps {
                sh 'docker run -d --name test_server server-testing1'
            }
        }
        stage('Realizar pruebas') {
            steps {
                sh 'pytest'
            }
        }
        stage('Detener contenedor') {
            steps {
                sh 'docker stop test_server'
            }
        }
    }
}
