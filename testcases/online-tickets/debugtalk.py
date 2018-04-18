import jwt
import time
import base64
import json
import hashlib
import hmac
import os
import requests

# useridA="252"
# usernameA="Etdaegg684"
# useridB="0"
# usernameB="Etddxnu343"
# timeStamp=""
userId = "208283"
userName = "Etdegcu275"
ticketId = 0

def create_token(uId, uname):
    print("---->uId: " + uId)

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
    
    token = jwt.encode(payload, signKey, algorithm="HS512")

    return token.decode("utf-8")

def verify_bearer_token(token):
    signKey = "adWqFeisdfD#1412$sdkf%23*afz&"
    payload = jwt.decode(token, signKey, algorithms=["HS512"])
    return payload

def create_timeStamp():
    global timeStamp
    millis = int(round(time.time()*1000))
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(millis/1000))
    timeStamp = now
    return timeStamp

def save_itemStamp(str):
    file = open("../tmp/timeStamp.txt", "w")
    file.write(str)
    file.close()

def get_itemId():
    tmp_path = os.path.abspath(os.path.join(os.getcwd(), "../../tmp"))
    timeStamp_path = os.path.join(tmp_path, "itemId.txt")
    file = open(timeStamp_path, "r")
    itemId = file.readline()
    file.close()
    print("---->itemId " + itemId)
    return itemId

def get_ticketId():
    global ticketId
    token = create_token(userId, userName)
    r = requests.get("http://10.20.9.179:9310/api/online-tickets/v1/tickets/unused",
                    headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
                            "Authorization": token
                    },
                    params={
                                "pageNum": "1",
                                "pageSize": "1",
                                "userId": "208283",
                                "type": "RED_PACKET",
                                "terminal": "PC"
                    }
        )
    if r.status_code == 200:
        print("---->reponse json: " + str(r.json()))
        rq_json = r.json()
        rq_text = r.text
        rq_json_m = json.loads(rq_text)
        print("---->rq_json: ")
        print(rq_json)
        print("---->rq_text: ")
        print(rq_text)
        print("rq_json_m: ")
        print(rq_json_m)
        for key in rq_json_m.keys():
            if key == "records":
                for dic in rq_json_m["records"]:
                    ticketId = dic["ticId"]
                    print(ticketId)

def save_ticketId():
    print("---->ticketId: " + str(ticketId))
    tmp_path = os.path.abspath(os.path.join(os.getcwd(), "../../tmp"))
    ticketId_path = os.path.join(tmp_path, "ticketId.txt")
    fopen = open(ticketId_path, "w")
    fopen.write(str(ticketId))
    fopen.close()

tokenUser = create_token(userId, userName)
itemId = get_itemId()
itemId_m = int(itemId)

print(tokenUser)
get_ticketId()
save_ticketId()


# def get_itemId():
#     tmp_path = os.path.abspath(os.path.join(os.getcwd(), "../../tmp"))
#     timeStamp_path = os.path.join(tmp_path, "timeStamp.txt")
#     file = open(timeStamp_path, "r")
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
