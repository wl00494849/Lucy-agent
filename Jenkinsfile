pipeline{
    agent any
    environment {
        IMAGE_NAME = "Lucy_agent"
        OPENAI_API_KEY = credentials('OPENAI_API_KEY')
    }
    stages{
        stage("Test"){
            steps{
                echo "testing..."
                def props = readProerties file: ''
                python3 -m unittest discover -s tests -v
            }
        }

        stage("Build Image"){
            steps{
                echo "building..."
                def version = "v${env.BUILD_NUMBER}"
                sh 'docker build -t ${IMAGE_NAME}:${version} -f dockerfile .'
                sh 'docker save ${IMAGE_NAME}:${version} -o ${IMAGE_NAME}.tar'
            }
        }

        stage("Deploy"){
            steps{
                echo "deploying..."
            }
        }
    }
}gpt