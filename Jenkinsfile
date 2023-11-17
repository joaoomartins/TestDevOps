pipeline {
    agent any

    triggers {
        cron('H/5 * * * *') // Dispara a cada 5 minutos
    }

    stages {
        stage('Notify Discord') {
            steps {
                script {
                    discordSend channel: 'nome-do-canal', color: 'good', message: 'Esta é uma mensagem de teste do Jenkins!'
                }
            }
        }
    }
}
