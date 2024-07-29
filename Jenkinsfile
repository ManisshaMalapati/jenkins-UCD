pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/ManisshaMalapati/jenkins-UCD.git'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'python -m venv venv'
                sh 'source venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }
    }
    
    post {
        always {
            junit '**/test-results/*.xml'
        }
    }
}
