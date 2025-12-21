pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Get the code from GitHub
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                // Build the Docker images
                sh 'docker-compose build'
            }
        }
        
        stage('Deploy') {
            steps {
                // Stop any old containers and start the new ones
                sh 'docker-compose down'
                sh 'docker-compose up -d'
            }
        }
    }
}
