pipeline {
    agent any
    environment {
        MAIN_PATH = '/home/lfgodoi/Documentos/Projetos/vibration-analysis-interface'
    }
    stages {
        stage('Removing running container') {
            steps {
                sh 'docker stop vai-container || true'
                sh 'docker rm vai-container || true'
            }        
        }
        stage('Remove existing image') {
            steps {
                sh 'docker rmi vai-image || true'
            }        
        }
        stage('Build the application image') {
            steps {
                sh 'docker build -t vai-image $MAIN_PATH'
            }        
        }
        stage('Run the application container') {
            steps {
                sh 'docker run -d -p 8000:8000 --name vai-container vai-image'
            }        
        }
    }
}