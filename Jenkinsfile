pipeline {
    agent any

    environment {
        IMAGE_NAME = 'dilnazkamil/fastapi-notes'
        IMAGE_TAG = 'latest'
    }

    stages {
        stage('Install dependencies') {
            steps {
                sh 'pip install --user -r requirements.txt'

            }
        }

        stage('Run tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build Docker image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .'
            }
        }

        stage('Push Docker image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push $IMAGE_NAME:$IMAGE_TAG
                    '''
                }
            }
        }

        stage('Deploy to Test Environment') {
            steps {
                sh 'kubectl apply -f k8s/test-deployment.yaml'
            }
        }

        stage('Deploy to Production') {
            when {
                branch 'main' 
            }
            steps {
                sh 'kubectl apply -f k8s/prod-deployment.yaml'
            }
        }
    }
}
