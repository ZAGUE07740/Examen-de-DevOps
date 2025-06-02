pipeline {
    agent any

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
                sh """
                    python3 --version || sudo apt-get update && sudo apt-get install -y python3 python3-pip
                    pip3 install --upgrade pip
                    pip3 install -r requirements.txt
                """
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
