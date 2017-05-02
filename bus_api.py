# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 16:52:04 2017

@author: James
"""

import requests
import json

payload = {
"apiKey":"87vGou@pHO9nhk2"
}
url = 'http://ikuass.kuas.edu.tw/User/GetAppVersion' # API URL  查詢版本號
r = requests.post(url, data=payload)
r = r.text
print r+"\n\n"

username = raw_input("Enter Your Account:")
password = raw_input("Enter Your Password:")

login = {
"apiKey":"87vGou@pHO9nhk2",
"userId":username,
"userPw":password,
"userKeep":"0"
}
url = 'http://ikuass.kuas.edu.tw/User/DoLogin' # API URL  登入

r = requests.post(url, data=login)
r = r.text
print r+"\n\n"

data  = json.loads(r)
apiKey = data['data']['userKey'] # 取得 apiKey

payload = {
"apiKey":apiKey,
"userId":username,
"busId":"34279",    #預約34279號校車
        }

url = 'http://ikuass.kuas.edu.tw/Bus/CreateUserReserve' # API URL  預約校車


r = requests.post(url, data=payload)
r = r.text
print r +"\n\n"
data  = json.loads(r)
print data['message']

