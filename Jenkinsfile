node('CentOS') {

	stage('clone code'){
		//checkout scm
		sh 'git clone git@github.com:1213adam/inspur_server_automation.git'
	}


	stage('run test'){
		echo 'run testing'
		sh 'run.sh'
	}

	stage('send report'){
		echo 'send report'
	}

}
