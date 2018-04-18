from requests_toolbelt import MultipartEncoder
import requests
import json

test_file="/Users/etongdai/Desktop/test2.png"

def upload():
    token = login()
    print(type(token))
    m = MultipartEncoder(fields={
            'file': ('test2.png', open(test_file, 'rb'), 'image/png')
        })
    print(type(m))
    print(m)
    r = requests.post('http://10.20.9.153:9010/api/usercenter/v2/informations/attachment',
                        data=m, 
                        headers={'Content-Type': m.content_type, 'Authorization': token} ,
                        params={
                                "attachmentName": "pic",
                                "attachmentType": "JB"
                        })
    print(r.status_code)
    print(r.json())

def login():
    payload = {
                "mobile": "18600001111",
                "oauthType": "ETONGDAI",
                "password": "3BCBE64170882B5C17627B7ACAFDA9EE"
            }
    r = requests.post('http://10.20.9.153:9010/api/usercenter/v2/auth/login',
                        data=json.dumps(payload),
                        headers={"Content-Type": "application/json", "Accept": "application/json"}  
                        )
    token = r.json()['token']
    print("---->" + r.url)
    return token

upload()