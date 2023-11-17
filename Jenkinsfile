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
                        webhookURL: 'https://discord.com/api/webhooks/1175144751914291241/3Y6JJVQmBmhOxU-ZNUcaoUhVddVKMD37EqovVsykQqXc9aZVCiayJb3h98rmGrhQ2N1i',
                        title: 'SAMUEL O FIXE',
                        thumbnail: 'https://cdn.discordapp.com/attachments/639547689310093342/1175145406808731669/294787720_5550552661664092_7421828174387227350_n.jpg?ex=656a2a72&is=6557b572&hm=efe41f1b0fc1c0df73f1e35b42ee8a8cdb3ceaa6c6fe9ee2dda107216efe44bd&0',
                        image:'https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.latercera.com%2Fresizer%2FwvCMr6B4HSnbYmlIGtaDQVfuch4%3D%2F900x600%2Fsmart%2Farc-anglerfish-arc2-prod-copesa.s3.amazonaws.com%2Fpublic%2FOI7WIZAY6NDH7AQHHZ2NLXTCX4.jpg&tbnid=FpUn-UUhi4D-zM&vet=12ahUKEwiKydvT2cuCAxUDnCcCHdCPDwQQMygBegQIARBP..i&imgrefurl=https%3A%2F%2Fwww.latercera.com%2Fmouse%2Fbob-esponja-memes-tributo%2F&docid=8L01nz3k7qUXYM&w=900&h=600&q=spongebob%20arcoiris&client=firefox-b-d&ved=2ahUKEwiKydvT2cuCAxUDnCcCHdCPDwQQMygBegQIARBP',
                        description: 'O Samuel é muita fixe!',
                        footer: 'Samu´s Leader',
                        result: currentBuild.currentResult
                    )
                }
            }
        }
    }
}
