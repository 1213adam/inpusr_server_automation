from ctypes import *
import os
current_path=os.path.abspath(__file__)
father_path=os.path.abspath(os.path.dirname(current_path)+os.path.sep+".")
so_lib_path=father_path+r"/../"+"shared_object/"
lib=cdll.LoadLibrary(so_lib_path+"allLinuxFunc.so")


def hello():
    lib.hello()

def add(int_a,int_b):
    sum=lib.add(int_a,int_b)
    return sum

def inc(int_a):
    forC_int_a=c_int(int_a) #conver parameter int_a into c type
    pt_int_a=POINTER(c_int)(forC_int_a) #conver forC_int into pointer
    return lib.inc(pt_int_a)


def printArr(alist):
    alist_c=(c_int*len(alist))(*alist) #change python arrary into c list
    alist_c_p=POINTER(c_int)(alist_c)   #change c list into c list pointer
    lib.printArr(alist_c_p,len(alist))


def getArr():
    lib.getArr.restype = POINTER(c_int)
    return lib.getArr()

def callFunc():
    lib.callFunc()


if __name__ == '__main__':
    callFunc()

