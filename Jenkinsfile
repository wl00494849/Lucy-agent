pipeline{
    agent any
    environment {
        IMAGE_NAME = "Lucy_agent"
        OPENAI_API_KEY = credentials('OPENAI_API_KEY')
    }
    stages{
        stage('Setup Python Env'){
            sh '''
                python3 -m venv venv
                . venv/bin/active
                pip3 install --upgrade pip
                if [ -f requirements.txt ]; then
                    pip3 install -r requirements.txt
                fi
            '''
        }

        stage("Test"){
            steps{
                echo "testing..."
                sh '''
                    python -m unittest discover -s tests -v
                '''
            }
        }

        stage("Build Image"){
            steps{
                echo "building..."
                def version = "v${env.BUILD_NUMBER}"
                sh '''
                    docker build -t ${IMAGE_NAME}:${version} -f dockerfile .
                    docker save ${IMAGE_NAME}:${version} -o ${IMAGE_NAME}.tar
                '''
            }
        }

        stage("Deploy"){
            steps{
                echo "deploying..."
            }
        }
    }
}gpt