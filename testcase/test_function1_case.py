from common_method import allLinuxFunc_method
from baseline import baseline
from testdata import testdata

def setup():
    print("this is setup .....")
def teardown():
    print("this is teardown .....")


def testcase001_hello():
    allLinuxFunc_method.hello()
    assert 1 ==baseline.testcase001_baseline

def testcase002_hello():
    allLinuxFunc_method.hello()
    assert 1 == baseline.testcase002_baseline


def testcase003_add():
    res=allLinuxFunc_method.add(testdata.testdata003[0],testdata.testdata003[1])
    assert res == baseline.testcase003_baseline

def testcase004_add():
    res = allLinuxFunc_method.add(testdata.testdata004[0],testdata.testdata004[1])
    assert res == baseline.testcase004_baseline

def testcase005_inc():
    res = allLinuxFunc_method.inc(testdata.testdata005)
    print(res)
    assert res == baseline.testcase005_baseline

def testcase006_inc():
    res = allLinuxFunc_method.inc(testdata.testdata006)
    print(res)
    assert res == baseline.testcase006_baseline

def testcase007_printArr():
    allLinuxFunc_method.printArr(testdata.testdata007)
    assert 1==baseline.testcase008_baseline

def testcase008_getArr():
    res = allLinuxFunc_method.getArr()
    print(res)
    assert 1==baseline.testcase008_baseline

def testcase009_callFunc():
    res = allLinuxFunc_method.callFunc()
    print(res)
    assert 1==baseline.testcase008_baseline

if __name__ == '__main__':
    testcase009_callFunc()