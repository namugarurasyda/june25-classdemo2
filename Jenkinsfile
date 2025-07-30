pipeline{
    agent any
    
    environment {
        VENV = 'venv'
    }

    stages {
        stage('checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/namugarurasyda/june25-classdemo2.git' //specify your repository url here
                
            }
        }
        stage('setup Virtual Environment'){
            steps{
                sh'''
                python3 -m venv venv
                .$VENV/bin/activate
                pip install -r requirements.txt


                 '''
            }
        }
        stage('Run Tests'){
                steps{
                    sh'''
                    .$VENV/bin/activate
                    pytest
                    '''
                }

        }
    }

}