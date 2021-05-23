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
                script {
                try {
                    sh '''
                        cmake  --build build --target install
                    '''
                } catch (err) {
                    echo err.getMessage()
                    sh '''
                        sed -i "/@value{srcdir}/d" src/toolchain/gcc/riscv-gcc/gcc/doc/invoke.texi
                        cmake  --build build --target install
                    '''
                }
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                sh """
                    RISCV_RND_ROOT=install ./src/tests/infra/smitest --labels checkin --wd ci_run
                """
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
