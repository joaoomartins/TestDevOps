pipeline {
    agent any

    triggers {
        cron('H/5 * * * *') 

    stages {
        stage('Notify Discord') {
            steps {
                script {
                    discordSend(
                        webhookURL: 'https://discord.com/api/webhooks/1175127066409173143/2ZG59FapKkdv3glyDEqd3r718RZcimUNv47iTsaLUXAMPNgiPzSwcnhnsejwonPGuIll',
                        description: 'Good Description',
                        footer: 'Nice footer',
                        result: currentBuild.currentResult,
                        title: JOB_NAME
                    )
                }
            }
        }
    }
}
