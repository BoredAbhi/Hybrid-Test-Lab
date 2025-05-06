pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'qa_hybrid_framework_image'
        DOCKER_TAG = 'latest'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm  // Checkout the code from the repository
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build -t $DOCKER_IMAGE:$DOCKER_TAG .'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run Behave tests inside the Docker container
                    sh 'docker run --rm $DOCKER_IMAGE:$DOCKER_TAG behave'
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                script {
                    // Generate Allure report from Behave's JSON result
                    sh 'docker run --rm -v $(pwd)/reports:/reports $DOCKER_IMAGE:$DOCKER_TAG allure generate /reports/behave_results.json --clean -o /reports/allure_report'
                }
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', reportBuildPolicy: 'ALWAYS', results: [[path: 'reports/allure_report']]
            }
        }
    }
}
