import os
current_path=os.path.abspath(__file__)
project_root_path=os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
testsuite_path=project_root_path+r"/testsuite"
rf_report_path=project_root_path+r"/rf_report"
print(rf_report_path,testsuite_path)
cmd="robot -P ./../ -d %s -r rf_report.html --reporttitle automation_testing_report --loglevel TRACE  %s " %(rf_report_path,testsuite_path)
print(cmd)
os.system(cmd)
