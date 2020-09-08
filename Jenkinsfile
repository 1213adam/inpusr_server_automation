node('CentOS') {

	stage('clone code'){
		//checkout scm
		sh 'rm -rf inspur_server_automation'
		sh 'git clone git@github.com:1213adam/inspur_server_automation.git'
	}


	stage('run test'){
		echo 'run testing'
		sh 'cd inspur_server_automation && chmod 777 *.sh *.py && run.sh'
	}

	stage('send report'){
		echo 'send report'
	}

}
