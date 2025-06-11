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
        ENV_FILE = '.env'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                bat """
                    echo Building Docker image: %DOCKER_IMAGE%
                    docker build -t %DOCKER_IMAGE% .
                """
            }
        }

        stage('Run Analysis') {
            steps {
                bat """
                    echo Running analysis with env file: %ENV_FILE%
                    docker run --env-file %ENV_FILE% %DOCKER_IMAGE%
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                    echo Running tests with env file: %ENV_FILE%
                    docker run --env-file %ENV_FILE% %DOCKER_IMAGE% pytest tests/ --cov=app --cov-report=term-missing
                """
            }
        }

        stage('Cleanup') {
            steps {
                bat """
                    echo Cleaning up Docker image
                    docker rmi %DOCKER_IMAGE%
                """
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
        success {
            echo 'Pipeline succeeded.'
        }
        failure {
            echo 'Pipeline failed.'
        }
        cleanup {
            echo 'Pruning unused Docker resources...'
            bat 'docker system prune -f'
        }
    }
}
