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
        withPythonEnv('python3') {
        sh 'python --version'
        echo 'building the application...'
        echo 'test'
        sh 'python --version'
        echo "building version ${NEW_VERSION}"
        sh "python3 keplerCheckIn.py $C4S_CREDENTIALS_USR $C4S_CREDENTIALS_PSW $RUECKERTSCRIPTS_CREDENTIALS_USR $RUECKERTSCRIPTS_CREDENTIALS_PSW"
      }
      }
    }

  }
}
