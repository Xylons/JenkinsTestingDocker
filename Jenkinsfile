pipeline {
  agent { label "master" }
  stages {
    stage("Executing Tests") {
      steps {
        sh "echo 1234 | sudo -S pytest tests.py"
      }
    }
    stage("build") {
      steps {
        sh "echo 1234 | sudo -S docker build -t calculator . "
      }
    }
    stage("run") {
      steps {
        sh "echo 1234 | sudo -S docker run --rm calculator"
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
