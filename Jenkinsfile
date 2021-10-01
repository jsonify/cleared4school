pipeline {
  agent any
  environment {
    NEW_VERSION = '1.3.0'
    C4S_CREDENTIALS = credentials('c4s-credentials')
    RUECKERTSCRIPTS_CREDENTIALS = credentials('rueckertscripts-credentials')
  }

  stages {
    stage("build") {
      steps {
        withPythonEnv('/usr/bin/python3') {
        sh 'pip install selenium'
        sh 'python --version'
        echo 'building the application...'
        echo 'test'
        sh 'which python'
        echo "building version ${NEW_VERSION}"
        sh "python3 keplerCheckIn.py $C4S_CREDENTIALS_USR $C4S_CREDENTIALS_PSW $RUECKERTSCRIPTS_CREDENTIALS_USR $RUECKERTSCRIPTS_CREDENTIALS_PSW"
      }
      }
    }

  }
}
