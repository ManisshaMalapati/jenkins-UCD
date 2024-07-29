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
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate'
                sh 'venv/bin/pip install --upgrade pip'
                sh 'venv/bin/pip install -r requirements.txt'
                sh 'venv/bin/pip install --upgrade numpy'
                sh 'venv/bin/pip install --upgrade pandas'
            }
        }
        
        stage('Run Tests') {
            steps {
                sh 'source venv/bin/activate'
                sh 'export PYTHONPATH=./ && venv/bin/pytest -v tests/'
            }
        }
    }
    
    post {
        always {
            junit '**/test-results/*.xml'
        }
    }
}
