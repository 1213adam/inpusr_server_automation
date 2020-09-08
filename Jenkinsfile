node('CentOS') {

	stage('clone code'){
		//checkout scm
		sh 'rm -rf inspur_server_automation'
		sh 'git clone git@github.com:1213adam/inspur_server_automation.git'
	}


	stage('run test'){
		echo 'run testing'
		sh 'cd inspur_server_automation && chmod 777 *.sh *.py && sh run.sh'
	}
	
	stage('run windows local test'){
		node(){
			bat 'dir'
		}
	}

	stage('send report'){
		echo 'send report'
		robot logFileName: 'log.html', outputFileName: 'output.xml', outputPath: 'inspur_server_automation/rf_report/', reportFileName: 'rf_report.html'
	}

}
