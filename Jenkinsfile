pipeline{
    agent any
    environment {
        BRANCH = 'main'
    }
    stages{
        stage("Git pull"){
            steps{
                echo "Obtendo a versão mais recente do projeto"
                git url: 'https://github.com/rfabriciors/flask-heroes.git', branch: "${BRANCH}"
            }
        }
        stage("Build Container Image"){
            steps{
                echo "Construindo a imagem Docker"
                script {
                    dockerapp = docker.build("rfabricio/flask-heroes:v${env.BUILD_NUMBER}-${BRANCH}",
                    '-f ./Dockerfile .')
                }
            }
        }
        stage("Push container to Docker Hub"){
            steps{
                echo "Executando o push das imagens para o Docker Hub"
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
                    dockerapp.push("latest")
                    dockerapp.push("v${env.BUILD_NUMBER}-${BRANCH}")
                    }
                }
            }
        }
        stage("Deploy to Kubernetes Cluster"){
            agent {
                kubernetes {
                    cloud 'kubernetes'
                }
            }
            steps{
                echo "Fazendo o deploy da aplicação no cluster Kubernetes"
                kubernetesDeploy(configs: '**/k8s/**', kubeconfigId: 'kubeconfig', enableConfigSubstitution: true)
            }
        }  
    }
}