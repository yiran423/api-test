import jwt
import time
import base64
import json
import hashlib
import hmac


def create_token():

	headers = json.dumps({
		"typ": "JWT",
		"alg": "HS256"
		})

	payload = {
    	"iss": "etongdai",
		"iat": int(time.time()),
		"exp": int(time.time()) + 86400 * 7,
		"sub": '{"userId": "206053", "username": "Etdaegg684"}'
    }
	
	signKey = "adWqFeisdfD#1412$sdkf%23*afz&"
	
	token = jwt.encode(payload, signKey, algorithm='HS512')

	return token
    

def verify_bearer_token(token):
	signKey = "adWqFeisdfD#1412$sdkf%23*afz&"
	payload = jwt.decode(token, signKey, algorithms=['HS512'])
	return payload


print(create_token())
print(verify_bearer_token(create_token()))

# print(jwt.__file__)
	