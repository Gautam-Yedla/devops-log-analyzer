// pipeline {
//     agent any

//     tools {
//       git 'Default'
//     }

//     environment {
//         EMAIL_USER = credentials('JenkinsGautamAdmin')   // ID in Jenkins credentials
//         EMAIL_PASS = credentials('JenkinsGautamAdmin')   // ID in Jenkins credentials
//     }

//     stages {
//         // stage('Clone') {
//         //     steps {
//         //         git 'https://github.com/Gautam-Yedla/devops-log-analyzer.git'
//         //     }
//         // }
//         stage('Build Docker Image') {
//             steps {
//                 bat 'docker build -t log-analyzer .'
//             }
//         }
//         stage('Run Analysis') {
//             steps {
//                 bat 'docker run -e EMAIL_USER=%EMAIL_USER% -e EMAIL_PASS=%EMAIL_PASS% log-analyzer'
//             }
//         }
//         stage('Run Tests') {
//             steps {
//                 bat "docker run -e EMAIL_USER=%EMAIL_USER% -e EMAIL_PASS=%EMAIL_PASS% log-analyzer pytest --cov=app --cov-report=term-missing"
//             }
//         }
//     }
// }

pipeline {
    agent any

    tools {
        git 'Default'
    }

    environment {
        DOCKER_IMAGE = 'log-analyzer:latest'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                bat "docker build -t %DOCKER_IMAGE% ."
            }
        }

        stage('Run Analysis') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'JenkinsGautamAdmin',
                        usernameVariable: 'EMAIL_USER',
                        passwordVariable: 'EMAIL_PASS'
                    )
                ]) {
                    bat """
                        docker run -e EMAIL_USER=%EMAIL_USER% -e EMAIL_PASS=%EMAIL_PASS% %DOCKER_IMAGE%
                    """
                }
            }
        }

        stage('Run Tests') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'JenkinsGautamAdmin',
                        usernameVariable: 'EMAIL_USER',
                        passwordVariable: 'EMAIL_PASS'
                    )
                ]) {
                    bat """
                        docker run -e EMAIL_USER=%EMAIL_USER% -e EMAIL_PASS=%EMAIL_PASS% %DOCKER_IMAGE% \
                        pytest tests/ --cov=app --cov-report=term-missing
                    """
                }
            }
        }
    }
}
