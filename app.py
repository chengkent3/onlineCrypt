from flask import Flask,render_template
from datetime import datetime
import re
import json

app = Flask(__name__)

@app.route('/show')
def home():
    return render_template('index.html', title='Home', message='Hello, World!')

def encrpyt_code(nums,sourceCode):
    newStr  = []
    for str in sourceCode:
        # print(ord(str))
        #print(int(ord(str))+int(nums))
        anum = int(ord(str))
        rnum = int(nums)
        if(anum<65 or ( anum>90 and anum<97 ) or anum >122 ):
            newStr.append(str)
            continue
        # print("before anum:{} rnum:{}",anum,rnum)
        if(anum+rnum>122 and anum <=122):
            rnum = 122-anum
            anum=97
        elif(anum+rnum >90 and anum <=90 ):
            rnum= 90-anum
            anum =65
        # print("anum:{} rnum:{}",anum,rnum)
        newStr.append(chr((anum+rnum)))
    print("after sourceCode:{} newStr:{}",sourceCode,newStr)
    # newStr.reverse()
    return newStr


@app.route("/encrypt/<int:nums>/<sourceCode>",methods = ['POST','GET'])
def encrpyt(nums,sourceCode):
    sCode =sourceCode
    encrpytStr= []


    if(int(nums)<=0):
        return {"code":503,"msg":"nums under 1"}
    
    for i in range(int(nums)):
        encrpytStr.reverse()
        encrpytStr= encrpyt_code(nums,sourceCode)
        sourceCode ="".join(encrpytStr)
    
    returnStr = {
        "sourceStr":sCode,
        "encrpytStr":"".join(encrpytStr),
        "code":200
        }
    return returnStr


def decrpyt_code(nums,encrpytCode):
    
    newStr  = []
    reversedStr =[]
    for str in encrpytCode:
        reversedStr.append(str)
    # reversedStr.reverse()
    # print("encrpytCode:{} reversedStr:{}",encrpytCode,reversedStr)
    for str in reversedStr:
        anum = int(ord(str))
        rnum = int(nums)
        print("before anum:{} rnum:{}",anum,rnum)
        if(anum<65 or ( anum>90 and anum<97 ) or anum >122 ):
            newStr.append(str)
            continue
        if(anum-rnum<97 and anum>=97):
            rnum = anum-97
            anum=122
        elif(anum-rnum <65 and anum >=65 ):
            rnum= anum-65
            anum =90
        # print(ord(str))
        print("after anum:{} rnum:{}",anum,rnum)

        newStr.append(chr((anum-rnum)))
    return newStr

@app.route("/decrypt/<int:nums>/<encrpytCode>",methods = ['POST','GET'])
def decrpyt(nums,encrpytCode):
    sCode =encrpytCode
    encrpytStr= []


    if(int(nums)<=0):
        return {"code":503,"msg":"nums under 1"}
    for i in range(int(nums)):
        encrpytStr.reverse()
        encrpytStr= decrpyt_code(nums,encrpytCode)
        encrpytCode ="".join(encrpytStr)
    returnStr = {
        "sourceStr":sCode,
        "encrpytStr":"".join(encrpytStr),
        "code":200,
        "msg":"success"
        }
    return returnStr

if __name__ == "__main__":  
  app.run(debug = True)