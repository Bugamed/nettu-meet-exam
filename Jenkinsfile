pipeline {
    agent any
    stages{
        stage('semgrep')
          }
}

























    agent { label 'docker-agent-alpine-jdk17'
        }
    stages {  
        stage('Static-sonar'){
            steps {
                script {
                scannerHome = tool 'main';}
                withSonarQubeEnv(installationName: 'sq9004u24') {
                sh "${scannerHome}/bin/sonar-scanner"
                }
            }
        }
        stage('SCA'){
            steps {
                script {
                    sh '''
                        apk add curl bash jq grype
                        curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sh -s -- -b /usr/local/bin
                        grype db update
                        grype . -o table > grype-report-chernyak.txt
                    '''
                    archiveArtifacts artifacts: 'grype-report-chernyak.txt', allowEmptyArchive: true
                }
            }
        }   
        stage('Static-semgrep') {
            steps {
                script {
                    //sh 'apk add docker'
                    sh 'apk add python3'
                    sh 'apk add --update pipx'
                    sh 'pipx install semgrep; pipx ensurepath; source ~/.bashrc'
                    sh '/root/.local/bin/semgrep scan --config auto > semgrep.txt'
                    //sh '/root/.local/bin/semgrep ci'
                    archiveArtifacts artifacts: 'semgrep.txt', allowEmptyArchive: true
                }
            }
        }
        stage('Static-sonar-qg') {
            steps {
                timeout(time: 10, unit: 'MINUTES') {
                waitForQualityGate abortPipeline: true
                }
                //script {
                    //def qg = waitForQualityGate(installationName: 'sq9004u24') 
                   // if (qg.status != 'OK') {
                    //    error "Quality Gate failed: ${qg.status}"
                    //}
                //}
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

