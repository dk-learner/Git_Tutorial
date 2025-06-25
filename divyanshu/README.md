### Basic Details
1. Name: Divyanshu
1. Company: C-DAC
1. User Id: [dk-learner](https://github.com/dk-learner)

### Commands to run

1. Jenkins installation
   ```
   docker run -d -v jenkins_home:/var/jenkins_home -p 8080:8080 -p 50000:50000 --restart=on-failure jenkins/jenkins:lts-jdk17
   ```
2. Get the jenkins password from docker logs
   ```
   docker logs <container_id> # Do docker ps for getting container ID
   ```
3. Install with suggested plugings
4. Create pipeline with basic steps (Compile, test, coverage)
   ```
   pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh "echo 'Build Success'"
            }
        }
        stage('Tests') {
            steps {
                sh "echo 'Test run Success'"
            }
        }
         stage('Coverage') {
            steps {
                sh "echo covered"
            }
        }
    }
}

   ```
