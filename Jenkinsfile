pipeline {
    agent any

    triggers {
        cron('H/5 * * * *') // Dispara a cada 5 minutos
    }

    stages {
        stage('Notify Discord') {
            steps {
                script {
                    discordSend(
                        webhookURL: 'https://discord.com/api/webhooks/1175127066409173143/2ZG59FapKkdv3glyDEqd3r718RZcimUNv47iTsaLUXAMPNgiPzSwcnhnsejwonPGuIll',
                        description: 'Really Good Description',
                        footer: 'Nice Footer',
                        result: currentBuild.currentResult,
                        title: JOB_NAME
                    )
                }
            }
        }
    }
}
