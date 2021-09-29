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
        echo 'building the application...'
        echo "building version ${NEW_VERSION}"
        sh "python3 keplerCheckIn.py $C4S_CREDENTIALS_USR $C4S_CREDENTIALS_PSW"
      }
    }
    
    stage("test") {
      
      steps {
        echo 'testing the application...'
      }
    }
    
    stage("deploy") {
      steps {
        echo 'deploying the application...'
      }
    }
  }
}
