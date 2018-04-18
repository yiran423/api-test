from requests_toolbelt import MultipartEncoder
from redis import Redis
import requests
import random
import string
import hashlib
import json
from requests_toolbelt.streaming_iterator import StreamingIterator

test_file="/Users/etongdai/Desktop/test2.png"
phone_number = "15801161111"

def make_user_info(avatar_file):
    fields = {
        'file': ('test2.png', open(avatar_file, 'rb'), 'image/png'),
    }
    print(fields.get('avatar'))
    return MultipartEncoder(fields)

def make_user_info():
    fields = {
        'file': ('test2.png', open(test_file, 'rb'), 'image/png')
    }
    print("making user info...")
    return MultipartEncoder(fields)

def get_content_type(multipart_encoder):
    return multipart_encoder.content_type

def get_phone():
    numbers = "15801161111"
    return numbers

def gen_strings():
    ran_strs = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    print(ran_strs)

def search_redis():
    r = Redis(host='10.20.9.54', port=6379, db=0)
    raw_b = r.get('imageCode_REGISTER_test')
    print(type(raw_b))
    str = raw_b.decode()
    print(type(str))
    print(str)

def upload():
    m = MultipartEncoder(fields={
            'file': ('test2.png', open(test_file, 'rb'), 'image/png')
        })
    r = requests.post('http://10.20.9.153:9010/api/usercenter/v2/informations/attachment', 
    					data=m, headers={'Content-Type': m.content_type, 'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ7XCJ1c2VySWRcIjoxLFwidXNlcm5hbWVcIjpcInRlc3RcIn0iLCJpc3MiOiJldG9uZ2RhaSIsImV4cCI6MTUyMjgxNTEyOCwiaWF0IjoxNTIyNjM1MTI4fQ.FSMbKxW8CX_smC-izblH2rP2vtiaDM-zlqVGCfRd-P2miOkPLcjfMamty5Q1TxvkSLJmcbSi-5wcKJfLSYELGw'}, 
    					params={
                    			"attachmentName": "pic",
                    			"attachmentType": "JB"
                		})
    print(r.status_code)

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
    # print("---->" + r.url)
    token = r.json()['token']
    return token

img = MultipartEncoder(fields={
            'file': ('test2.png', open(test_file, 'rb'), 'image/png')
        })
ctype = img.content_type

token = login()


# print(make_user_info(test_file))
# make_user_info(test_file)

print("running debugtalk")
# search_redis()
#print(make_user_info())

# gen_strings()

# print(get_phone())
# multipart_encoder=make_user_info()
# multipart_type=get_content_type(multipart_encoder)
# multipart_body="thisthisthis"

#upload()

