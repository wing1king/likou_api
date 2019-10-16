import requests
import datetime
import unittest
import time

# 测试环境
base_url = "http://119.29.1.133"
# 开发环境
# base_url: http://10.72.17.30
# 预发布环境
# base_url: https://sandbox-riko-xms.uu.cc
# 正式环境
# base_url: http://api-riko-xms.uu.cc

#headres


# 获取access_token
def get_token():
    data = {
            'openid': '164b4571e4542ca8f2cc19776f7fd2f211111',
            'uid': 99999999999,	# 170****2087手机号
            'sessionid': 'a9d384dd8ca7a22ec38505ddaf03eb6605b6a62661',
            }
    res = requests.post(url= base_url + '/app/user/login', json=data)
    return "Bearer " + res.json()['data']['access_token']


headers = {
        "Authorization": get_token(),
        "access_type": '2',
        "channel": '',
        "content-type": "text/plain",
        "deviceid": '',
        "from": '3',
        "sign": "7756948fcaecc936531065b2e1167a8c",
        "version": "1.0.0"  
}










