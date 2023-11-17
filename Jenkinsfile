pipeline {
    agent any

    triggers {
        cron('H/10 * * * *')
    }

    stages {
        stage('Notify Discord') {
            steps {
                script {
                    discordSend(
                        webhookURL: 'https://discord.com/api/webhooks/1175144751914291241/3Y6JJVQmBmhOxU-ZNUcaoUhVddVKMD37EqovVsykQqXc9aZVCiayJb3h98rmGrhQ2N1i',
                        title: 'SAMUEL O FIXE',
                        image: 'https://cdn.discordapp.com/attachments/639547689310093342/1175145406808731669/294787720_5550552661664092_7421828174387227350_n.jpg?ex=656a2a72&is=6557b572&hm=efe41f1b0fc1c0df73f1e35b42ee8a8cdb3ceaa6c6fe9ee2dda107216efe44bd&0',
                        description: ' @everyone O Samuel é muita fixe!',
                        footer: 'Samuel do Papel',
                        result: currentBuild.currentResult
                    )
                }
            }
        }
    }
}
