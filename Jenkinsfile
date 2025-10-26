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
                docker build -t python-gpt:pi -f dockerfile .
                docker save python-gpt:pi -o python-gpt.tar
                sh ''
            }
        }


        stage("Deploy"){
            steps{
                echo "deploying..."
            }
        }
    }
}