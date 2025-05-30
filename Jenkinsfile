pipeline {
    pipeline {
    agent {
        docker {
            image 'python:3.12-slim'
        }
    }

    environment {
        DOCKER_USERNAME = "zague07"
        DOCKER_CREDENTIALS = credentials("credentials_id_jenkins")
        IMAGE_VERSION = "1.${BUILD_NUMBER}"
        DOCKER_IMAGE = "${DOCKER_USERNAME}/examen-de-devops:${IMAGE_VERSION}"
        DOCKER_CONTAINER = "examen-de-devops-app-${BUILD_NUMBER}"
    }

    stages {
        stage("Checkout") {
            steps {
                git branch: 'main', url: 'https://github.com/ZAGUE07740/Examen-de-DevOps.git', credentialsId: 'credentials_id_jenkins'
            }
        }

        stage("Test") {
            steps {
                sh "pip install -r requirements.txt"
                sh "apt-get update && apt-get install -y python3-pip"
                sh "pip install --upgrade pip"
    
                // sh "python manage.py check"
            }
        }

        stage("Build Docker Image") {
            steps {
                sh "docker build -t $DOCKER_IMAGE ."
            }
        }

        stage("Push image to Docker Hub") {
            steps {
                sh """
                    echo $DOCKER_CREDENTIALS_PSW | docker login -u $DOCKER_CREDENTIALS_USR --password-stdin
                    docker push $DOCKER_IMAGE
                """
            }
        }

        stage("Deploy Container") {
            steps {
                sh """
                    docker rm -f $DOCKER_CONTAINER || true
                    docker run -d --name $DOCKER_CONTAINER -p 8000:8000 $DOCKER_IMAGE
                """
            }
        }
    }
}
