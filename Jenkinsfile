pipeline{
    agent any

    environment {
        VENV_DIR = 'venv'
        GCP_PROJECT = "mlops-hotel-reservation-508001"
        GCLOUD_PATH = "/usr/bin"
    }

    stages{
        stage('Cloning Github repo to Jenkins'){
            steps{
                script{
                    echo 'Cloning Github repo to Jenkins............'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token1', url: 'https://github.com/ankitumare/mlops_hotel_reservation.git']])
                }
            }
        }

    }

}