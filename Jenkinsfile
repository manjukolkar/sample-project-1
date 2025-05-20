pipeline {
    agent any

    environment {
        IMAGE_NAME = 'manjukolkar007/student-feedback'
        CONTAINER_NAME = 'student-feedback-container'
        PORT = '5000'
    }

    stages {
        stage('Git Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/manjukolkar/sample-project-1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build --no-cache -t ${IMAGE_NAME}:latest ."
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                    }
                }
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                sh "docker push ${IMAGE_NAME}:latest"
            }
        }

        stage('Deploy to MicroK8s') {
            steps {
                sh '''
                microk8s kubectl apply -f k8s/deployment.yaml
                microk8s kubectl apply -f k8s/service.yaml
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed. No local container cleanup required.'
        }
    }
}
