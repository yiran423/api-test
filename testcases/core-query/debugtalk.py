import requests
import json
import time
import os
import re

useridA="252"
usernameA="Etdaegg684"
useridB="0"
usernameB="Etddxnu343"
timeStamp=""
timeStamp_path=""
index=""

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
    token = jwt.encode(payload, signKey, algorithm="HS512")
    return token.decode("utf-8")

def verify_bearer_token(token):
    signKey = "adWqFeisdfD#1412$sdkf%23*afz&"
    payload = jwt.decode(token, signKey, algorithms=["HS512"])
    return payload

def search_item():
    url = "http://10.20.9.132:8890/api/core/v1/items/investments"
    global index
    itemName = get_itemName()
    print("---->itemName: " + itemName)
    itemName_m = itemName[:-3]
    print("---->itemName_m: " + itemName_m)
    itemsList = []
    payload = {
                "byProgress": "1", 
                "byLimit": "1", 
                "repayType": "1", 
                "pageSize": "1000", 
                "yearRate": "2", 
                "currPage": "1", 
                "byInterest": "1", 
                "timeLimit": "6", 
                "isFixed": "0"
                }
    headers = {}
    r = requests.get(url, params=payload)
    if r.status_code == 200:
        print("status_code 200!!!")
        rq_json = json.loads(r.text)
        # print(r.text)
        # print("----> title:" + rq_json["data"][2]["title"])
        print("----> count:" + str(rq_json["count"]))
        for key in rq_json.keys():
            print("key: " + key)
            if key == "data":
                for dic in rq_json["data"]:
                    print(dic["title"])
                    if dic["title"].find(itemName_m) >= 0:
                        index = rq_json["data"].index(dic)
                        print("index---->" + str(index))
                        itemId = dic["iteId"]
                        print("itemId: " + str(dic["iteId"]))
                        print("title is ok")
                        itemsList.append(itemId)
        print("itemId contains: " + str(itemsList))
    itemId = ",".join(str(i) for i in itemsList)
    print("---->itemId: " + itemId)
    print("---->itemId type: " + str(type(itemId)))
    return itemId, index

def create_timeStamp():
    global timeStamp
    millis = int(round(time.time()*1000))
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(millis/1000))
    timeStamp = now
    return timeStamp

def save_itemStamp(str):
    file = open(timeStamp_path, "w")
    file.write(str)
    file.close()

def get_tmp_path():
    global timeStamp_path
    tmp_path = os.path.abspath(os.path.join(os.getcwd(), "../../tmp"))
    timeStamp_path = os.path.join(tmp_path, "timeStamp.txt")
    print(timeStamp_path)

def get_itemName():
    tmp_path = os.path.abspath(os.path.join(os.getcwd(), "../../tmp"))
    timeStamp_path = os.path.join(tmp_path, "timeStamp.txt")
    file = open(timeStamp_path, "r")
    itemStamp = file.readline()
    file.close()
    itemName = "liushuo api test " + itemStamp
    print(itemName)
    return itemName

def replace_json():
    assert_iteId = "content.data.%s.iteId" % index
    print("---->>>" + assert_iteId)
    fopen = open("investmentsSearch.json", "r")
    wstr = ""
    for line in fopen:
        if re.search('"replaceforanything"', line):
            line = re.sub('"replaceforanything"', '"%s"', line) % assert_iteId
            wstr += line
        elif re.search("6666", line):
            line = re.sub("6666", "%d", line) % int(itemId)
            wstr += line
        else:
            wstr += line
    print(wstr)
    wopen = open("investmentsSearch.json", "w")
    wopen.write(wstr)
    fopen.close()
    wopen.close()

def refresh_json():
    wstr = ""
    i=0
    with open("investmentsSearch.json", "r+") as fopen:
        lines = fopen.readlines()
        while i  < len(lines):
            print("---->line numbers begin " + str(i))
            line = lines[i]
            if re.search('"content.data.*"', line):
                line = re.sub('"content.data.*"', '"replaceforanything"', line)
                wstr += line
                i+=1
                line = lines[i]
                line = re.sub("\d+", "6666", line)
                wstr += line
                print("---->line numbers " + str(i))
            else:
                wstr += line
            i+=1
    print(wstr)
    wopen = open("investmentsSearch.json", "w")
    wopen.write(wstr)
    fopen.close()
    wopen.close()

def get_itemId():
    pass

def save_itemId():
    print("---->" + itemId)
    tmp_path = os.path.abspath(os.path.join(os.getcwd(), "../../tmp"))
    itemId_path = os.path.join(tmp_path, "itemId.txt")
    fopen = open(itemId_path, "w")
    fopen.write(itemId)
    fopen.close()

def setup_hook_replace(method, url, kwargs):
    print("---->hook running")
    replace_json()

def teardown_hook_refresh(resp_obj):
    refresh_json()

itemId,index=search_item()

print("---->" + "itemId: " + itemId + "\n---->index: " + str(index))

replace_json()

save_itemId()

# print("---->" + assert_iteId)

# itemName=get_itemName()
# get_tmp_path()
# create_timeStamp()
# print(timeStamp)
# save_itemStamp(timeStamp)

    # print(r.url + "\n------------------------\n" + r.text)

# search_item()

# tokenA = create_token(useridA, usernameA)
# tokenB = create_token(useridB, usernameB)
# print(tokenA)
# print(tokenB)
# print(verify_bearer_token(tokenA))
# print(verify_bearer_token(tokenB))

# print(jwt.__file__)
    
