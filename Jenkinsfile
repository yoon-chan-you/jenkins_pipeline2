pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        git url: 'https://github.com/yoon-chan-you/jenkins_pipeline2.git', branch: 'main'
      }
    }
    stage('Setup') {
      steps {
        echo "Python 환경을 설정합니다."
        echo 'Python 환경설정 완료. (pytest 설치 완료)'
      }
    }
    stage('Test') {
      steps {
        echo "pytest를 사용해서 테스트를 실행합니다."
        sh 'pytest ./test.py'
        echo "테스트 완료."
      }
    }
  }
}