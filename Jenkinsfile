pipeline {
    agent {
        docker {
            image 'python:3.10' 
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

        stage("Install & Test") {
            steps {
                sh '''
                    python3 --version
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    # python manage.py test
                '''
            }
        }

        stage("Build Docker Image") {
            agent {
                label 'docker-host' 
            }
            steps {
                sh "docker build -t $DOCKER_IMAGE ."
            }
        }

        stage("Push image to Docker Hub") {
            agent {
                label 'docker-host'
            }
            steps {
                sh """
                    echo $DOCKER_CREDENTIALS_PSW | docker login -u $DOCKER_CREDENTIALS_USR --password-stdin
                    docker push $DOCKER_IMAGE
                """
            }
        }

        stage("Deploy Container") {
            agent {
                label 'docker-host'
            }
            steps {
                sh """
                    docker rm -f $DOCKER_CONTAINER || true
                    docker run -d --name $DOCKER_CONTAINER -p 8000:8000 $DOCKER_IMAGE
                """
            }
        }
    }
}
