import jwt
import time
import base64
import json
import hashlib
import hmac
import os

useridA="252"
usernameA="Etdaegg684"
useridB="0"
usernameB="Etddxnu343"
timeStamp=""
timeStamp_m=""

def create_token(uId, uname):
    print(uId)

    headers = json.dumps({
        "typ": "JWT",
        "alg": "HS256"
        })

    payload = {
        "iss": "etongdai",
        "iat": int(time.time()),
        "exp": int(time.time()) + 86400 * 7,
        "sub": '{"userId": "%s", "username": "%s"}' % (uId, uname)
    }
    
    signKey = "adWqFeisdfD#1412$sdkf%23*afz&"
    
    token = jwt.encode(payload, signKey, algorithm='HS512')

    return token.decode('utf-8')


def verify_bearer_token(token):
    signKey = "adWqFeisdfD#1412$sdkf%23*afz&"
    payload = jwt.decode(token, signKey, algorithms=['HS512'])
    return payload

def create_timeStamp():
    global timeStamp
    millis = int(round(time.time()*1000))
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(millis/1000))
    timeStamp = now
    return timeStamp

def save_itemStamp(str):
    tmp_path = os.path.abspath(os.path.join(os.getcwd(), "../../tmp"))
    timeStamp_path = os.path.join(tmp_path, "timeStamp.txt")
    print("---->" + timeStamp_path)
    file = open(timeStamp_path, 'w')
    file.write(str)
    file.close()

def get_itemName():
    tmp_path = os.path.abspath(os.path.join(os.getcwd(), "../../tmp"))
    timeStamp_path = os.path.join(tmp_path, "timeStamp.txt")
    file = open(timeStamp_path, 'r')
    itemTimeStamp = file.readline()
    file.close()
    itemName = "liushuo api test " + itemTimeStamp
    print("---->itemName: " + itemName)
    return itemName

def remove_second():
    global timeStamp
    print("---->removing timeStamp: " + timeStamp)
    timeStamp_m = timeStamp[:-3]
    print("---->removed timeStamp: " + timeStamp_m)

def get_itemId():
    tmp_path = os.path.abspath(os.path.join(os.getcwd(), "../../tmp"))
    timeStamp_path = os.path.join(tmp_path, "itemId.txt")
    file = open(timeStamp_path, 'r')
    itemId = file.readline()
    file.close()
    print("---->itemId " + itemId)
    return itemId

# def get_itemId():
#     tmp_path = os.path.abspath(os.path.join(os.getcwd(), "../../tmp"))
#     timeStamp_path = os.path.join(tmp_path, "timeStamp.txt")
#     file = open(timeStamp_path, 'r')
#     itemId = file.read()

tokenA = create_token(useridA, usernameA)
tokenB = create_token(useridB, usernameB)
print(tokenA)
print(tokenB)
print(verify_bearer_token(tokenA))
print(verify_bearer_token(tokenB))

create_timeStamp()
print(timeStamp)
save_itemStamp(timeStamp)

remove_second()

itemId = get_itemId()
itemId_m = int(itemId)

get_itemName()




