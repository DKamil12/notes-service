pipeline {
    agent {
        docker {
            image 'python:3.10-slim'
        }
    }

    stages {
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh 'pytest'
            }
        }
    }
}
