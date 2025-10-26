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
                sh 'sudo docker build -t python-gpt:pi -f dockerfile .'
                sh 'sudo docker save python-gpt:pi -o python-gpt.tar'
            }
        }


        stage("Deploy"){
            steps{
                echo "deploying..."
            }
        }
    }
}