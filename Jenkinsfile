pipeline {
    agent any

    environment {
        // Identifiants Docker Hub
        DOCKER_USERNAME = "ton_username_dockerhub"
        DOCKER_CREDENTIALS = credentials("ton_credentials_id_jenkins")
        IMAGE_VERSION = "1.${BUILD_NUMBER}"
        DOCKER_IMAGE = "${DOCKER_USERNAME}/examen-de-devops:${IMAGE_VERSION}"
        DOCKER_CONTAINER = "examen-de-devops-app"
    }

    stages {
        stage("Checkout") {
            steps {
                git branch: 'main', url: 'https://github.com/ZAGUE07740/Examen-de-DevOps.git'
            }
        }

        stage("Test") {
            steps {
                echo "Exécution des tests Django..."
                bat "pip install -r requirements.txt"
                bat "python manage.py check"
            }
        }

        stage("Build Docker Image") {
            steps {
                bat "docker build -t %DOCKER_IMAGE% ."
            }
        }

        stage("Push image to Docker Hub") {
            steps {
                bat """
                    echo %DOCKER_CREDENTIALS_PSW% | docker login -u %DOCKER_CREDENTIALS_USR% --password-stdin
                    docker push %DOCKER_IMAGE%
                """
            }
        }

        stage("Deploy Container") {
            steps {
                bat """
                    docker rm -f %DOCKER_CONTAINER% || exit 0
                    docker run -d --name %DOCKER_CONTAINER% -p 8000:8000 %DOCKER_IMAGE%
                """
            }
        }
    }

    post {
        success {
            mail to: 'tezagre86@gmail.com',
                 subject: "Succès: Déploiement ${env.JOB_NAME} [${env.BUILD_NUMBER}]",
                 body: "Le déploiement s'est terminé avec succès."
        }
        failure {
            mail to: 'tezagre86@gmail.com',
                 subject: "Échec: Déploiement ${env.JOB_NAME} [${env.BUILD_NUMBER}]",
                 body: "Le déploiement a échoué. Veuillez vérifier Jenkins."
        }
    }
}
