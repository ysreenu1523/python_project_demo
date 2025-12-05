pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://your-git-repo-url.git'
            }
        }
        stage('Setup Environment') {
            steps {
                sh '''
                python -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run Script') {
            steps {
                sh '''
                source venv/bin/activate
                python src/main.py
                '''
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
