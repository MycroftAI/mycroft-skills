pipeline {
    agent any
    options {
        // Running builds concurrently could cause a race condition with
        // building the Docker image.
        disableConcurrentBuilds()
        // Only keep the last 5 builds.
        buildDiscarder(logRotator(numToKeepStr: '5'))
    }
    stages {
        stage('Run Integration Tests') {
            when {
                anyOf {
                    changeRequest()
                }
            }
            environment {
                //spawns GITHUB_USR and GITHUB_PSW environment variables
                GITHUB=credentials('c5770310-9e46-4ab1-84d4-bb17ae2b2bfb')
            }
            steps {
                sh 'docker build \
                    --build-arg major_release=20.02 \
                    --build-arg platform=mycroft_mark_1 \
                    --build-arg pull_request=$BRANCH_NAME \
                    --build-arg branch_name=$CHANGE_BRANCH \
                    --build-arg github_user=$GITHUB_USR \
                    --build-arg github_password=$GITHUB_PSW \
                    --no-cache \
                    -t voight-kampff-skill:$BRANCH_NAME .'
                echo 'Running Tests'
                timeout(time: 60, unit: 'MINUTES')
                {
                    sh 'docker run \
                        --volume "$HOME/voight-kampff/identity:/root/.mycroft/identity" \
                        --volume "$HOME/voight-kampff/:/root/allure" \
                        voight-kampff-skill:$BRANCH_NAME \
                        -f allure_behave.formatter:AllureFormatter \
                        -o /root/allure/allure-result --tags ~@xfail'
                }
            }
            post {
                always {
                    echo 'Report Test Results'
                    sh 'mv $HOME/voight-kampff/allure-result allure-result'
                    script {
                        allure([
                            includeProperties: false,
                            jdk: '',
                            properties: [],
                            reportBuildPolicy: 'ALWAYS',
                            results: [[path: 'allure-result']]
                        ])
                    }
                    unarchive mapping:['allure-report.zip': 'allure-report.zip']
                    sh (
                        label: 'Publish Report to Web Server',
                        script: '''scp allure-report.zip root@157.245.127.234:~;
                            ssh root@157.245.127.234 "unzip -o ~/allure-report.zip";
                            ssh root@157.245.127.234 "rm -rf /var/www/voight-kampff/skills/${BRANCH_NAME}";
                            ssh root@157.245.127.234 "mv allure-report /var/www/voight-kampff/skills/${BRANCH_NAME}"
                        '''
                    )
                    echo 'Report Published'
                }
            }
        }
    }
    post {
        cleanup {
            sh(
                label: 'Docker Container and Image Cleanup',
                script: '''
                    docker container prune --force;
                    docker image prune --force;
                '''
            )
        }
    }
}
