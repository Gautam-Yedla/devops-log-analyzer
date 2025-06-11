pipeline {
    agent any

    tools {
      git 'Default'
    }

    environment {
        EMAIL_USER = credentials('JenkinsGautamAdmin')   // ID in Jenkins credentials
        EMAIL_PASS = credentials('JenkinsGautamAdmin')   // ID in Jenkins credentials
    }

    stages {
        // stage('Clone') {
        //     steps {
        //         git 'https://github.com/Gautam-Yedla/devops-log-analyzer.git'
        //     }
        // }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t log-analyzer .'
            }
        }
        stage('Run Analysis') {
            steps {
                bat 'docker run -e EMAIL_USER=%EMAIL_USER% -e EMAIL_PASS=%EMAIL_PASS% log-analyzer'
            }
        }
        stage('Run Tests') {
            steps {
                bat "docker run -e EMAIL_USER=%EMAIL_USER% -e EMAIL_PASS=%EMAIL_PASS% log-analyzer pytest --cov=app --cov-report=term-missing"
            }
        }
    }
}
