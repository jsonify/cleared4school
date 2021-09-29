pipeline {
  agent any
  environment {
    NEW_VERSION = '1.3.0'
  }
  
  stages {
    stage("build") {
      steps {
        echo 'building the application...'
        echo "building version ${NEW_VERSION}"
        withCredentials([
          usernamePassword(credentials: 'c4s-credentials', usernameVariable: USER, passwordVariable: PASSWORD)
        ]) {
          echo "some script: ${USER}:${PASSWORD}"
        }
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
