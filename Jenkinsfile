pipeline {
    agent any
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
                bat 'docker run log-analyzer'
            }
        }
    }
}
