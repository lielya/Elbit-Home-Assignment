node {    
    stage('Clone repository') {
        git credentialsId: 'git_login', url: 'https://github.com/lielya/Elbit-Home-Assignment'
    }
    stage('Build image') {
    	dockerImage = docker.build('web_app:latest')
    }
    stage('Push image') {
        withDockerRegistry([ credentialsId: "docker_login", url: 'https://hub.docker.com/' ]) {
            dockerImage.push()
        }
    }
}

