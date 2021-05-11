pipeline {
    agent any
    stages {
        stage('Fetching submodules') {
            steps {
                echo 'Fetching submodules...'
                sh """
                    git submodule update --init --remote
                """
            }
        }
        stage('Configuring components') {
            steps {
                echo "Configuring components..."
                sh """
                    mkdir install && \
                    mkdir build && cd build && \
                    cmake ../ -DCMAKE_INSTALL_PREFIX=../install
                """
            }
        }
        stage('Building components') {
            steps {
                echo "Building components..."
                sh 'cd ./build && make'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
