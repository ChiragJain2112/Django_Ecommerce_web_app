pipeline {
    agent {label 'dev-agent'}
    
    stages{
        stage('code'){
            steps{
                git url: 'https://github.com/ChiragJain2112/Django_Ecommerce_web_app' , branch: 'master'
            }
        }
        stage('Test'){
            steps{
                sh 'docker build . -t chiragjain21/ecommerce-cicd:latest'
            }
        }
        stage('Login and Push Image'){
            steps{
                echo 'Login and pushing into docker hub'
                withCredentials([usernamePassword(credentialsId :'dockerhub',passwordVariable:'dockerHubPassword',usernameVariable:'dockerHubUser')]){
                     sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
                     sh "docker push ${env.dockerHubUser}/ecommerce-cicd:latest"
                }
            }
        }
        stage('Deploy'){
            steps{
                sh 'docker-compose down && docker-compose up -d'
            }
        }
    }
}
