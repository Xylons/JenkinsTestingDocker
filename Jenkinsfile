pipeline {
  agent { label "master" }
  stages {
    stage("Executing Tests") {
      steps {
        sh "pytest tests.py"
      }
    }
    stage("build") {
      steps {
        sh "echo 1234 | sudo -S docker build -t hello_there . "
      }
    }
    stage("run") {
      steps {
        sh "echo 1234 | sudo -S docker run --rm hello_there"
      }
    }
  }
    post{
    success{
      emailext (
          subject: "Fallo en la pipeline del proyecto: TEST",
            body: "La build de ${env.BUILD_URL} se ha completado",
            to: "fco.lamata@alu.uclm.es"
       )
    }
    failure{
        emailext (
          subject: "Fallo en la pipeline del proyecto: TEST",
            body: "La build de ${env.BUILD_URL} ha fallado",
            to: "fco.lamata@alu.uclm.es"
       )
    }
  }
}
