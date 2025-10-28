pipeline{
    agent any

    environment {
        IMAGE_NAME = 'lucy_agent'
        OPENAI_API_KEY = credentials('OPENAI_API_KEY')
    }

    stages{
        stage('Set Env'){
            steps{
                script{
                    env.VERSION = "v1.${env.BUILD_NUMBER}"
                    env.REGISTRY = sh(script: 'getent hosts host.docker.internal | awk \'{print $1}\' || true', returnStdout: true).trim()
                }
            }
        }
        stage('Setup Python Env & Testing'){
            agent {
                // 環境隔離
                docker {
                    image 'python:3.12-slim'   
                    args '-u root -e OPENAI_API_KEY=${OPENAI_API_KEY}'        
                }
            }

            steps{
                sh '''
                pip install --upgrade pip
                if [ -f requirements.txt ]; then
                    pip install -r requirements.txt
                fi
                pip install packaging
                echo '==========testing==========='
                export TEST_MODE=True
                python -m unittest discover -s tests -v
                '''
            }
        }

        stage('Build Image'){
            steps{
                echo "building..."
                script{
                    sh """
                        docker build -t ${env.REGISTRY}:5000/${IMAGE_NAME}:${env.VERSION} -f dockerfile .
                    """
                }
            }
        }
        stage('Push Image'){
            steps{
                echo "pushing"
                script{
                    sh"""
                        docker push ${env.REGISTRY}:5000/${IMAGE_NAME}:${env.VERSION}
                    """
                }
            }
        }
    }
}