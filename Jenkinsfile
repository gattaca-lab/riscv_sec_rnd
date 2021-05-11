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
        stage('Building components') {
            steps {
                echo 'Building components...'
                sh """
                    mkdir install
                    INSTALL_PATH=$(realpath ./install)
                    mkdir build && cd build
                    cmake ../ -DCMAKE_INSTALL_PREFIX=${INSTALL_PATH}

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
}
