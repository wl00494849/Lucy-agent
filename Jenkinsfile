pipeline{
    agent any

    environment {
        IMAGE_NAME = 'lucy_agent'
        OPENAI_API_KEY = credentials('OPENAI_API_KEY')
    }

    stages{
        stage('Setup Python Env & Testing'){
            agent {
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
                echo '==========testing==========='
                export TEST_MODE=True
                python -m unittest discover -s tests -v
                '''
            }
        }

        stage('Build Image & Push'){
            steps{
                echo "building..."
                script{
                    def version = "v1.${env.BUILD_NUMBER}"
                    def registry = sh(script: 'getent hosts host.docker.internal | awk \'{print $1}\' || true', returnStdout: true).trim()
                    sh """
                        docker build -t ${registry}:5000/${IMAGE_NAME}:${version} -f dockerfile .
                        docker push ${registry}:5000/${IMAGE_NAME}:${version}
                    """
                }
            }
        }   
    }
}