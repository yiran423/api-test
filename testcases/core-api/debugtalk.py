import jwt
import time
import base64
import json
import hashlib
import hmac
import os

# useridA="252"
# usernameA="Etdaegg684"
# useridB="0"
# usernameB="Etddxnu343"
# timeStamp=""
userId = "208283"
userName = "Etdegcu275"

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
    file = open('../tmp/timeStamp.txt', 'w')
    file.write(str)
    file.close()

def get_itemId():
    tmp_path = os.path.abspath(os.path.join(os.getcwd(), "../../tmp"))
    timeStamp_path = os.path.join(tmp_path, "itemId.txt")
    file = open(timeStamp_path, 'r')
    itemId = file.readline()
    file.close()
    print("---->itemId " + itemId)
    return itemId

def get_ticketId():
    tmp_path = os.path.abspath(os.path.join(os.getcwd(), "../../tmp"))
    timeStamp_path = os.path.join(tmp_path, "ticketId.txt")
    file = open(timeStamp_path, 'r')
    ticketId = file.readline()
    file.close()
    print("---->ticketId " + itemId)
    return ticketId

tokenUser = create_token(userId, userName)
itemId = get_itemId()
itemId_m = int(itemId)
ticketId=get_ticketId()

print(tokenUser)
# def get_itemId():
#     tmp_path = os.path.abspath(os.path.join(os.getcwd(), "../../tmp"))
#     timeStamp_path = os.path.join(tmp_path, "timeStamp.txt")
#     file = open(timeStamp_path, 'r')
#     itemId = file.read()

# tokenA = create_token(useridA, usernameA)
# tokenB = create_token(useridB, usernameB)
# print(tokenA)
# print(tokenB)
# print(verify_bearer_token(tokenA))
# print(verify_bearer_token(tokenB))

# create_timeStamp()
# print(timeStamp)
# save_itemStamp(timeStamp)
