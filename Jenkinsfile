pipeline{
    agent any
    evnvironment{
        IMAGE_NAME = "Lucy_agent"
    }
    stages{
        stage("Test"){
            steps{
                echo "testing..."
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