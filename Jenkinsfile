pipeline{
    agent any

    environment {
        IMAGE_NAME = "Lucy_agent"
        OPENAI_API_KEY = credentials('OPENAI_API_KEY')
    }

    stages{
        stage("Setup Python Env & Testing"){
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
                echo 'testing'
                python -m unittest discover -s tests -v
                '''
            }
        }

        stage("Build Image"){
            steps{
                echo "building..."
                script{
                    def version = "v${env.BUILD_NUMBER}"
                    sh '''
                        docker build -t ${IMAGE_NAME}:${version} -f dockerfile .
                        docker save ${IMAGE_NAME}:${version} -o ${IMAGE_NAME}.tar
                    '''
                }
            }
        }

        stage("Deploy"){
            steps{
                echo "deploying..."
            }
        }
    }
}