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
                        title: 'SAMUEL O SOLTEIRO',
                        thumbnail: 'https://instagram.fopo5-2.fna.fbcdn.net/v/t51.2885-19/278344658_1140398010054357_7407558841359093701_n.jpg?stp=dst-jpg_s320x320&_nc_ht=instagram.fopo5-2.fna.fbcdn.net&_nc_cat=109&_nc_ohc=bZGPaOoekrcAX_cKEQw&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfDu8srdyOB6N7zPckdrFz3j-sELbd5RpUW2Sh_Pgqe3Wg&oe=655D2CC9&_nc_sid=8b3546',
                        image: 'https://cdn.discordapp.com/attachments/639547689310093342/1175145406808731669/294787720_5550552661664092_7421828174387227350_n.jpg?ex=656a2a72&is=6557b572&hm=efe41f1b0fc1c0df73f1e35b42ee8a8cdb3ceaa6c6fe9ee2dda107216efe44bd&0',
                        description: ' @everyone O Samuel tá livre e solteiro!',
                        footer: 'Samuel do Papel (O CHEFE)',
                        result: currentBuild.currentResult
                    )
                }
            }
        }
    }
}
