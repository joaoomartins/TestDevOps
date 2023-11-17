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
                        webhookURL: 'https://discordapp.com/api/webhooks/https://discord.com/api/webhooks/1175108883811946535/wCTFqb4VcO1krkMP_PggBP0ifQkDZHaGL42tF_L1Lbqpv7oty_Xu3V8wX9b-TkbroAXL'  // Substitua pelo seu URL de webhook
                    )
                }
            }
        }
    }
}
