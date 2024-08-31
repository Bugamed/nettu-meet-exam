pipeline {
    agent any
    stages{
        /*stage('semgrep'){
            steps{
                sh '''
                apk add python3
                apk add --update pipx
                pipx install semgrep; pipx ensurepath; source ~/.bashrc
                /root/.local/bin/semgrep scan --config auto --json > semgrep.json
                '''
                archiveArtifacts artifacts: 'semgrep.json', allowEmptyArchive: true
            }
        }*/
        stage('trivy'){
            agent {
                label 'dind'
            }
            steps{
                sh'''
                docker run -v ./report:/report aquasec/trivy repo https://github.com/Bugamed/nettu-meet-exam -f json -o /report/trivy.json
                '''
                archiveArtifacts artifacts: 'report/trivy.json', allowEmptyArchive: true
            }
        }
        stage('zap'){
            steps{
                script{
                    sh 'echo "zap"'
                }
            }
        }
        stage('deptrack'){
            steps {
                script{
                    sh 'echo "dpt"'
                }
            }
        }
        stage('defectdojo'){
            steps{
                script{
                    sh 'echo "dojo"'
                }
            }
        }
        stage('QG'){
            steps{
                script{
                    sh 'echo "qg"'
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    sh 'echo "mama"'
                }
            }
        }
        stage('Dynamic') {
            steps {
                script {
                    sh 'echo "papa"'
                }
            }
        }
    }
    post {
        always {
            echo 'Pipeline завершен.'
        }
        success {
            echo 'Pipeline выполнен успешно!'
        }
        failure {
            echo 'Pipeline завершился с ошибкой.'
        }
    }
}
