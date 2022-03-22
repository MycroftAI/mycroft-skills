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
            options {
                lock(resource: "lock_${env.JOB_NAME}")
            }
            environment {
                //spawns GITHUB_USR and GITHUB_PSW environment variables
                GITHUB=credentials('devops-mycroft_mycroft-skills-vk-tests')
                // Some branches have a "/" in their name (e.g. feature/new-and-cool)
                // Some commands, such as those tha deal with directories, don't
                // play nice with this naming convention.  Define an alias for the
                // branch name that can be used in these scenarios.
                BRANCH_ALIAS = sh(
                    script: 'echo $BRANCH_NAME | sed -e "s#/#_#g"',
                    returnStdout: true
                ).trim()
            }
            steps {
                echo "Pushing to temporary test repo..."
                sh 'git remote add mine git+ssh://git@github.com/forslund/mycroft-skills.git || true'
                sh 'git push -uf mine ${BRANCH_NAME}'
                sh 'docker build \
                    --build-arg major_release=21.2.1 \
                    --build-arg platform=mycroft_mark_1 \
                    --build-arg pull_request=$BRANCH_NAME \
                    --build-arg branch_name=$BRANCH_NAME \
                    --build-arg repo_url=https://github.com/forslund/mycroft-skills \
                    --build-arg github_api_key=$GITHUB_PSW \
                    --no-cache \
                    --label build=${JOB_NAME} \
                    -t voight-kampff-skill:${BRANCH_ALIAS} .'
                echo 'Running Tests'
                timeout(time: 100, unit: 'MINUTES')
                {
                    sh 'mkdir -p $HOME/skills/$BRANCH_ALIAS/allure'
                    sh 'mkdir -p $HOME/skills/$BRANCH_ALIAS/mycroft-logs'
                    sh 'docker run \
                        --volume "$HOME/voight-kampff/identity:/root/.config/mycroft/identity" \
                        --volume "$HOME/skills/$BRANCH_ALIAS/allure:/root/allure" \
                        --volume "$HOME/skills/$BRANCH_ALIAS/mycroft-logs:/var/log/mycroft" \
                        --label build=${JOB_NAME} \
                        voight-kampff-skill:${BRANCH_ALIAS} \
                        -f allure_behave.formatter:AllureFormatter \
                        -o /root/allure/allure-result --tags ~@xfail'
                }
            }
            post {
                always {
                    echo 'Report Test Results'
                    echo 'Changing ownership of allure results...'
                    sh 'docker run \
                        --volume "$HOME/skills/$BRANCH_ALIAS/allure:/root/allure" \
                        --entrypoint=/bin/bash \
                        --label build=${JOB_NAME} \
                        voight-kampff-skill:${BRANCH_ALIAS} \
                        -x -c "chown $(id -u $USER):$(id -g $USER) \
                        -R /root/allure/"'
                    echo 'Changing ownership of Mycroft logs...'
                    sh 'docker run \
                        --volume "$HOME/skills/$BRANCH_ALIAS/mycroft-logs:/var/log/mycroft" \
                        --entrypoint=/bin/bash \
                        --label build=${JOB_NAME} \
                        voight-kampff-skill:${BRANCH_ALIAS} \
                        -x -c "chown $(id -u $USER):$(id -g $USER) \
                        -R /var/log/mycroft/"'

                    echo 'Transferring...'
                    sh 'rm -rf allure-result/*'
                    sh 'mv $HOME/skills/$BRANCH_ALIAS/allure/allure-result allure-result'
                    // This directory should now be empty, rmdir will intentionally fail if not.
                    sh 'rmdir $HOME/skills/$BRANCH_ALIAS/allure'
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
                    sh 'zip mycroft-logs.zip -r $HOME/skills/$BRANCH_ALIAS/mycroft-logs'
                    sh 'rm -rf $HOME/skills/$BRANCH_ALIAS/mycroft-logs'
                    // This directory should now be empty, rmdir will intentionally fail if not.
                    sh 'rmdir $HOME/skills/$BRANCH_ALIAS'
                    sh (
                        label: 'Publish Report to Web Server',
                        script: '''
                            ssh root@157.245.127.234 "mkdir -p ~/allure-reports/skills/${BRANCH_ALIAS}";
                            scp allure-report.zip root@157.245.127.234:~/allure-reports/skills/${BRANCH_ALIAS}/;
                            ssh root@157.245.127.234 "unzip -o ~/allure-reports/skills/${BRANCH_ALIAS}/allure-report.zip -d ~/allure-reports/skills/${BRANCH_ALIAS}/";
                            ssh root@157.245.127.234 "rm -rf /var/www/voight-kampff/skills/${BRANCH_ALIAS}";
                            ssh root@157.245.127.234 "mv ~/allure-reports/skills/${BRANCH_ALIAS}/allure-report /var/www/voight-kampff/skills/${BRANCH_ALIAS}"
                            ssh root@157.245.127.234 "rm ~/allure-reports/skills/${BRANCH_ALIAS}/allure-report.zip";
                            ssh root@157.245.127.234 "rmdir ~/allure-reports/skills/${BRANCH_ALIAS}";
                            ssh root@157.245.127.234 "mkdir -p ~/mycroft-logs/skills/${BRANCH_ALIAS}";
                            scp mycroft-logs.zip root@157.245.127.234:~/mycroft-logs/skills/${BRANCH_ALIAS}/;
                            ssh root@157.245.127.234 "mkdir -p /var/www/voight-kampff/skills/${BRANCH_ALIAS}/logs"
                            ssh root@157.245.127.234 "unzip -oj ~/mycroft-logs/skills/${BRANCH_ALIAS}/mycroft-logs.zip -d /var/www/voight-kampff/skills/${BRANCH_ALIAS}/logs/";
                            ssh root@157.245.127.234 "rm ~/mycroft-logs/skills/${BRANCH_ALIAS}/mycroft-logs.zip";
                            ssh root@157.245.127.234 "rmdir ~/mycroft-logs/skills/${BRANCH_ALIAS}";
                        '''
                    )
                    echo 'Report Published'
                }
                failure {
                    // Send allure report to Pull request
                    script {
                        // Create comment for Pull Requests
                        if (env.CHANGE_ID) {
                            echo 'Sending PR comment'
                            pullRequest.comment('Voight Kampff Integration Test Failed ([Results](https://reports.mycroft.ai/skills/' + env.BRANCH_ALIAS + ')). ' +
                                                '\nMycroft logs are also available: ' +
                                                '[skills.log](https://reports.mycroft.ai/skills/' + env.BRANCH_ALIAS + '/logs/skills.log), ' +
                                                '[audio.log](https://reports.mycroft.ai/skills/' + env.BRANCH_ALIAS + '/logs/audio.log), ' +
                                                '[voice.log](https://reports.mycroft.ai/skills/' + env.BRANCH_ALIAS + '/logs/voice.log), ' +
                                                '[bus.log](https://reports.mycroft.ai/skills/' + env.BRANCH_ALIAS + '/logs/bus.log), ' +
                                                '[enclosure.log](https://reports.mycroft.ai/skills/' + env.BRANCH_ALIAS + '/logs/enclosure.log)')
                        }
                    }
                    // Send failure email containing a link to the Jenkins build
                    // the results report and the console log messages to Mycroft
                    // developers, the developers of the pull request and the
                    // developers that caused the build to fail.
                    echo 'Sending Failure Email'
                    emailext (
                        attachLog: true,
                        subject: "FAILURE - Skills Integration Tests - Build ${BRANCH_NAME} #${BUILD_NUMBER}",
                        body: """
                            <p>
                                One or more integration tests failed. Use the
                                resources below to identify the issue and fix
                                the failing tests.
                            </p>
                            <br>
                            <p>
                                <a href='${BUILD_URL}'>
                                    Jenkins Build Details
                                </a>
                                &nbsp(Requires account on Mycroft's Jenkins instance)
                            </p>
                            <br>
                            <p>
                                <a href='https://reports.mycroft.ai/skills/${BRANCH_ALIAS}'>
                                    Report of Test Results
                                </a>
                            </p>
                            <br>
                            <p>
                                Mycroft logs are also available:
                                <ul>
                                    <li><a href='https://reports.mycroft.ai/skills/${BRANCH_ALIAS}/logs/skills.log'>skills.log</a></li>
                                    <li><a href='https://reports.mycroft.ai/skills/${BRANCH_ALIAS}/logs/audio.log'>audio.log</a></li>
                                    <li><a href='https://reports.mycroft.ai/skills/${BRANCH_ALIAS}/logs/voice.log'>voice.log</a></li>
                                    <li><a href='https://reports.mycroft.ai/skills/${BRANCH_ALIAS}/logs/bus.log'>bus.log</a></li>
                                    <li><a href='https://reports.mycroft.ai/skills/${BRANCH_ALIAS}/logs/enclosure.log'>enclosure.log</a></li>
                                </ul>
                            </p>
                            <br>
                            <p>Jenkins console log is attached.</p>""",
                        replyTo: 'devops@mycroft.ai',
                        to: 'dev@mycroft.ai',
                        recipientProviders: [
                            [$class: 'RequesterRecipientProvider'],
                            [$class:'CulpritsRecipientProvider'],
                            [$class:'DevelopersRecipientProvider']
                        ]
                    )
                }
                success {
                    // Send report to Pull request
                    script {
                        if (env.CHANGE_ID) {
                            echo 'Sending PR comment'
                            pullRequest.comment('Voight Kampff Integration Test Succeeded  ([Results](https://reports.mycroft.ai/skills/' + env.BRANCH_ALIAS + '))')
                        }
                    }
                    // Send success email containing a link to the Jenkins build
                    // and the results report to Mycroft developers, the developers
                    // of the pull request and the developers that caused the
                    // last failed build.
                    echo 'Sending Success Email'
                    emailext (
                        subject: "SUCCESS - Skills Integration Tests - Build ${BRANCH_NAME} #${BUILD_NUMBER}",
                        body: """
                            <p>
                                All integration tests passed. No further action required.
                            </p>
                            <br>
                            <p>
                                <a href='${BUILD_URL}'>
                                    Jenkins Build Details
                                </a>
                                &nbsp(Requires account on Mycroft's Jenkins instance)
                            </p>
                            <br>
                            <p>
                                <a href='https://reports.mycroft.ai/skills/${BRANCH_ALIAS}'>
                                    Report of Test Results
                                </a>
                            </p>""",
                        replyTo: 'devops@mycroft.ai',
                        to: 'dev@mycroft.ai',
                        recipientProviders: [
                            [$class: 'RequesterRecipientProvider'],
                            [$class:'CulpritsRecipientProvider'],
                            [$class:'DevelopersRecipientProvider']
                        ]
                    )
                }
            }
        }
    }
    post {
        success {
            // Docker images should remain upon failure for troubleshooting purposes.  However,
            // if the stage is successful, there is no reason to look back at the Docker image.  In theory
            // broken builds will eventually be fixed so this step should run eventually for every PR
            sh(
                label: 'Delete Docker Image on Success',
                script: '''
                    docker image prune --all --force --filter label=build=${JOB_NAME};
                '''
            )
        }
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
