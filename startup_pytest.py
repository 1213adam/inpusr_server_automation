import os

#generated path according the project root path,
current_path=os.path.abspath(__file__)
project_root_path=os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
py_report_path=project_root_path+r"/py_report"
testcase_path=project_root_path+r"/testcase"
allure_path=project_root_path+r"/allure_report"

cmd="pytest  %s --html=%s/pyreport.html --alluredir=%s --self-contained-html " % (testcase_path,py_report_path,allure_path)
os.system(cmd)

#genearted allure html report(suggest deploy this step into Jenkins)
# cmd="allure generate /home/xliang/inpusr_server_automation/allure_report/ -o /opt/apache-tomcat-9.0.37/webapps/auto_report"