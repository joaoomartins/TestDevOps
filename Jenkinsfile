pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Adicione os passos de compilação aqui
                sh 'echo "Building..."'
            }
        }

        stage('Test') {
            steps {
                // Adicione os passos de teste aqui
                sh 'echo "Testing..."'
            }
        }

        stage('Deploy') {
            steps {
                // Adicione os passos de implantação aqui
                sh 'echo "Deploying..."'
            }
        }
    }

    post {
        success {
            script {
                def changeLogSets = currentBuild.changeSets
                def commits = []

                changeLogSets.each { set ->
                    set.items.each { item ->
                        commits.add([
                            "author": item.author.fullName,
                            "message": item.msg
                        ])
                    }
                }

                def message = "Build successful! :white_check_mark:\n\nCommits:\n${commits.inspect()}"
                discordSend(
                    color: '00ff00', // Cor verde para sucesso
                    message: message,
                    webhookUrl: 'https://discord.com/api/webhooks/1175108883811946535/wCTFqb4VcO1krkMP_PggBP0ifQkDZHaGL42tF_L1Lbqpv7oty_Xu3V8wX9b-TkbroAXL'
                )
            }
        }

        failure {
            script {
                def message = "Build failed! :x:"
                discordSend(
                    color: 'ff0000', // Cor vermelha para falha
                    message: message,
                    webhookUrl: 'https://discord.com/api/webhooks/1175108883811946535/wCTFqb4VcO1krkMP_PggBP0ifQkDZHaGL42tF_L1Lbqpv7oty_Xu3V8wX9b-TkbroAXL'
                )
            }
        }
    }
}

// Função para enviar notificações para o Discord
def discordSend(Map params) {
    script {
        def payload = """
        {
            "content": "${params.message}",
            "embeds": [
                {
                    "title": "Jenkins Build",
                    "description": "${params.message}",
                    "color": ${params.color}
                }
            ]
        }
        """
        def response = httpRequest(
            acceptType: 'APPLICATION_JSON',
            contentType: 'APPLICATION_JSON',
            httpMode: 'POST',
            requestBody: payload,
            url: params.webhookUrl
        )

        echo "Discord notification response: ${response}"
    }
}
