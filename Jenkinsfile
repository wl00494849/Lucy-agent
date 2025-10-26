pipeline{
    agent any

    stages{
        stage("test"){
            steps{
                echo "testing..."
                python3 -m unittest discover -s tests -v
            }
        }

        stages("build"){
            steps{
                echo "building..."
            }
        }


        stage("deploy"){
            steps{
                echo "deploying..."
            }
        }
    }
}