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
                    cmake . -DCMAKE_INSTALL_PREFIX=install -Bbuild
                """
            }
        }
        stage('Building components') {
            steps {
                echo "Building components..."
                sh """
                    cmake  --build build --target install
                """
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
