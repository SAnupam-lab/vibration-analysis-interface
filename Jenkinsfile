pipeline {
    agent any
    environment {
        MAIN_PATH = '/home/lfgodoi/Documentos/Projetos/vibration-analysis-interface'
    }
    stages {
        stage('Delete running containers') {
            steps {
                sh 'sudo k3s kubectl delete deployment deployment-m1 || true'
                sh 'sudo k3s kubectl delete svc svc-m1 || true'
            }        
        }
    }
}