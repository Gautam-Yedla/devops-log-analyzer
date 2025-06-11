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
                sh 'docker build -t log-analyzer .'
            }
        }
        stage('Run Analysis') {
            steps {
                sh 'docker run log-analyzer'
            }
        }
    }
}
