pipeline {
    agent any

    environment {
        // Identifiants Docker Hub
        DOCKER_USERNAME = "zague07"
        DOCKER_CREDENTIALS = credentials("credentials_id_jenkins")
        IMAGE_VERSION = "1.${BUILD_NUMBER}"
        DOCKER_IMAGE = "${DOCKER_USERNAME}/examen-de-devops:${IMAGE_VERSION}"
        DOCKER_CONTAINER = "examen-de-devops-app-${BUILD_NUMBER}"
    }

    stages {
        stage("Checkout") {
            steps {
                // Cloner le dépôt GitHub
                git branch: 'main', url: 'https://github.com/ZAGUE07740/Examen-de-DevOps.git', credentialsId:"credentials_id_jenkins"
            }
        }

        stage("Test") {
            steps {
                echo "Exécution des tests Django..."
                sh "pip install -r requirements.txt"
                sh "python manage.py check"
            }
        }

        stage("Build Docker Image") {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }

        stage("Push image to Docker Hub") {
            steps {
                script {
                    sh """
                        echo ${DOCKER_CREDENTIALS_PSW} | docker login -u ${DOCKER_CREDENTIALS_USR} --password-stdin
                        docker push ${DOCKER_IMAGE}
                    """
                }
            }
        }

        stage("Deploy Container") {
            steps {
                script {
                    // Arrêter et supprimer l’ancien conteneur s’il existe
                    sh """
                        docker rm -f ${DOCKER_CONTAINER} || true
                        docker run -d --name ${DOCKER_CONTAINER} -p 8000:8000 ${DOCKER_IMAGE}
                    """
                }
            }
        }
    }

    post {
        success {
            mail to: 'ezagre86@gmail.com ',
                 subject: "Succès: Déploiement ${env.JOB_NAME} [${env.BUILD_NUMBER}]",
                 body: "Le déploiement s'est terminé avec succès."
        }
        failure {
            mail to: 'ezagre86@gmail.com ',
                 subject: "Échec: Déploiement ${env.JOB_NAME} [${env.BUILD_NUMBER}]",
                 body: "Le déploiement a échoué. Veuillez vérifier Jenkins."
        }
    }
}
