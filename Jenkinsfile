pipeline {
  agent any

  triggers {
        cron('0 8 * * 1-5')
  }

  environment {
    NEW_VERSION = '1.3.0'
    C4S_CREDENTIALS = credentials('c4s-credentials')
    RUECKERTSCRIPTS_CREDENTIALS = credentials('rueckertscripts-credentials')
  }

  stages {
    stage('Setup') { // Install any dependencies you need to perform testing
          steps {
            withPythonEnv('/usr/bin/python3') {
              sh 'pip install -r requirements.txt'
            }
          }
        }

    stage("build") {
      steps {
        withPythonEnv('/usr/bin/python3') {
          sh "python3 keplerCheckIn.py $C4S_CREDENTIALS_USR $C4S_CREDENTIALS_PSW $RUECKERTSCRIPTS_CREDENTIALS_USR $RUECKERTSCRIPTS_CREDENTIALS_PSW"
        }
      }
    }
  }
}
