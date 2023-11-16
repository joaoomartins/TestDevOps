pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'ls -la'
            }
        }
        stage('Test') {
            steps {
                script{
                    proprieties([
                        parameters([
                            choice(
                                choices: ['ONE', 'TWO'],
                                name: 'PARAMETER_01'
                            ),
                            text(
                                defaultValue: '''
                                this is a multi-line
                                string parameter example
                                ''',
                                name: 'MULTI-LINE-STRING'
                            ),
                            string(
                                defaultValue:'scriptcrunch',
                                name: 'STRING-PARAMETER',
                                trim: true
                            )
                        ])
                    ])
                }
                echo 'Testing.. $BOOLEAN'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}