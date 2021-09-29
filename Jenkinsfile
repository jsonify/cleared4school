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
          usernamePassword(credentialsId: 'c4s-credentials', usernameVariable: 'USER', passwordVariable: 'PWD')
        ]) {
          echo "some script: ${USER}: PWD"
          sh "python testingHello.py ${USER} ${PWD}"
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
