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
                        image: 'https://cdn.discordapp.com/attachments/1150574273174458398/1175246820520251393/Screenshot_20231118-004826_BeReal-01.jpg?ex=656a88e5&is=655813e5&hm=7ce19ff1cbc7e21ed706f598719a962b6864828589c3e0a84da22e734c4ac792&',
                        description: '@everyone Vocês são todos uns nabos!',
                        footer: 'Samuel do Papel (O CHEFE)',
                        result: currentBuild.currentResult
                    )
                }
            }
        }
    }
}
