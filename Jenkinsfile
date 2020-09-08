node('CentOS') {

	stage('clone code'){
		checkout scm
	}


	stage('run test'){
		echo 'run testing'
		sh 'run.sh'
	}

	stage('send report'){
		echo 'send report'
	}

}