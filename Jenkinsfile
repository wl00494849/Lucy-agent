pipeline{
    agent any

    stages{
        stage("Test"){
            steps{
                echo "testing..."
            }
        }

        stage("Build Image"){
            steps{
                echo "building..."
                sh 'DOCKER_BUILDKIT=1 docker build -t python-gpt:pi -f dockerfile .'
                sh 'docker save python-gpt:pi -o python-gpt.tar'
            }
        }


        stage("Deploy"){
            steps{
                echo "deploying..."
            }
        }
    }
}