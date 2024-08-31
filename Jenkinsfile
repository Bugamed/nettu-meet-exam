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
        stage('trivy'){
            agent {
                label 'dind'
            }
            steps{
                sh '''
                docker run -v \$(pwd)/:/report dockerhub.timeweb.cloud/aquasec/trivy repo https://github.com/Bugamed/nettu-meet-exam -f json -o /report/trivy.json
                '''
                archiveArtifacts artifacts: 'trivy.json', allowEmptyArchive: true
            }
        }
        stage('zap'){
            agent {
                label 'dind'
            }
            steps{
                script{
                    sh '''
                    docker run -v \$(pwd)/:/zap/wrk/:rw -t dockerhub.timeweb.cloud/zaproxy/zap-stable zap-baseline.py -I -t https://s410-exam.cyber-ed.space:8084 -J zap.json  
                    '''
                    archiveArtifacts artifacts: 'zap.json', allowEmptyArchive: true
                }
            }
        }
        /*stage('deptrack'){
            steps {
                script{
                    sh '''
                    curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin
                    syft dir:$(pwd) -o cyclonedx-xml@1.5 > sbom.xml

                    curl -k -X "PUT" "https://s410-exam.cyber-ed.space:8081/api/v1/bom" \
                    -H 'Content-Type: application/json' \
                    -H 'X-API-Key: odt_SfCq7Csub3peq7Y6lSlQy5Ngp9sSYpJl' \
                    -d '{
                        "project": "e24b8a18-0695-4ec0-b7fe-25e6e14b22d6",
                        "bom": {
                            "format": "CycloneDX",
                            "data": "'$(sbom.json)'"
                                }
                        }'
                    '''
                    archiveArtifacts artifacts: 'sbom.json', allowEmptyArchive: true
                }
            }
        }*/
        stage('defectdojo'){
            steps{
                script{
                    sh '''
                    curl --insecure -X 'POST' \
                    'https://s410-exam.cyber-ed.space:8083/api/v2/import-scan/' \
                    -H 'accept: application/json' \
                    -H 'Authorization: Token c5b50032ffd2e0aa02e2ff56ac23f0e350af75b4' \
                    -H 'Content-Type: multipart/form-data' \
                    -H 'X-CSRFTOKEN: nurNnjql2zjlKVv4vMkW6kLjCzcjEl7iWIychPLgmkQ3lTMo9BpHtSbIaeUG7bOb' \
                    -F 'active=true' \
                    -F 'verified=true' \
                    -F 'close_old_findings=false' \
                    -F 'deduplication_on_engagement=true' \
                    -F 'push_to_jira=false' \
                    -F 'minimum_severity=Info' \
                    -F 'close_old_findings_product_scope=false' \
                    -F 'apply_tags_to_endpoints=true' \
                    -F 'create_finding_groups_for_all_findings=true' \
                    -F 'apply_tags_to_findings=true' \
                    -F 'product_name=mchernyak' \
                    -F 'file=@semgrep.json;type=application/json' \
                    -F 'auto_create_context=true' \
                    -F 'scan_type=Semgrep JSON Report' \
                    -F 'engagement=55'

                    
                    curl --insecure -X 'POST' \
                    'https://s410-exam.cyber-ed.space:8083/api/v2/import-scan/' \
                    -H 'accept: application/json' \
                    -H 'Authorization: Token c5b50032ffd2e0aa02e2ff56ac23f0e350af75b4' \
                    -H 'Content-Type: multipart/form-data' \
                    -H 'X-CSRFTOKEN: nurNnjql2zjlKVv4vMkW6kLjCzcjEl7iWIychPLgmkQ3lTMo9BpHtSbIaeUG7bOb' \
                    -F 'active=true' \
                    -F 'verified=true' \
                    -F 'close_old_findings=false' \
                    -F 'deduplication_on_engagement=true' \
                    -F 'push_to_jira=false' \
                    -F 'minimum_severity=Info' \
                    -F 'close_old_findings_product_scope=false' \
                    -F 'apply_tags_to_endpoints=true' \
                    -F 'create_finding_groups_for_all_findings=true' \
                    -F 'apply_tags_to_findings=true' \
                    -F 'product_name=mchernyak' \
                    -F 'file=@zap.json;type=application/json' \
                    -F 'auto_create_context=true' \
                    -F 'scan_type=ZAP Scan' \
                    -F 'engagement=57'
                    '''
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
