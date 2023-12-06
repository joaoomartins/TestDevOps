pipeline {
    agent any

    triggers {
        cron('* * * * *')
    }

    stages {
        stage('Notify Discord') {
            steps {
                script {
                    discordSend(
                        webhookURL: 'https://discord.com/api/webhooks/1175144751914291241/3Y6JJVQmBmhOxU-ZNUcaoUhVddVKMD37EqovVsykQqXc9aZVCiayJb3h98rmGrhQ2N1i',
                        title: 'SAMUEL O SOLTEIRO',
                        link: 'https://www.instagram.com/samuelventura12321/',
                        thumbnail: 'https://instagram.fopo5-2.fna.fbcdn.net/v/t51.2885-19/278344658_1140398010054357_7407558841359093701_n.jpg?stp=dst-jpg_s320x320&_nc_ht=instagram.fopo5-2.fna.fbcdn.net&_nc_cat=109&_nc_ohc=bZGPaOoekrcAX_cKEQw&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfDu8srdyOB6N7zPckdrFz3j-sELbd5RpUW2Sh_Pgqe3Wg&oe=655D2CC9&_nc_sid=8b3546',
                        image: 'https://cdn.discordapp.com/attachments/1042760153222615044/1176278505286283435/Imagem_WhatsApp_2023-06-04_as_00.39.26_0d4a83b6.jpg?ex=656e49b9&is=655bd4b9&hm=57eb82b1fcde285938a6929ebc5944df75cd3f71334c229cf9cf89e69776381d&',
                        description: '@everyone Vocês são todos uns nabos!',
                        footer: 'Samuel do Papel ( O CHEFE)',
                        result: currentBuild.currentResult
                    )
                }
            }
        }
    }
}
