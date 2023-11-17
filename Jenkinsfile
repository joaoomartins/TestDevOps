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
                        color: 'good',   // Cor da mensagem (pode ser 'good', 'warning', 'danger', etc.)
                        message: 'Esta é uma mensagem de teste do Jenkins!',
                        webhookURL: 'https://discordapp.com/api/webhooks/https://discord.com/api/webhooks/1175127066409173143/2ZG59FapKkdv3glyDEqd3r718RZcimUNv47iTsaLUXAMPNgiPzSwcnhnsejwonPGuIll'  // Substitua pelo seu URL de webhook
                    )
                }
            }
        }
    }
}
