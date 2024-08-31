pipeline {
    agent any
    stages{
        stage('semgrep'){
            steps{
                sh '''
                apk add python3
                apk add --update pipx
                pipx install semgrep; pipx ensurepath; source ~/.bashrc
                /root/.local/bin/semgrep scan --config auto --json > semgrep.json
                '''
                archiveArtifacts artifacts: 'semgrep.json', allowEmptyArchive: true
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
