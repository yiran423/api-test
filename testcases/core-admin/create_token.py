import jwt
import time

# 使用 sanic 作为restful api 框架 
def create_token(request):
    grant_type = request.json.get('grant_type')
    username = request.json['username']
    password = request.json['password']
    if grant_type == 'password':
        account = verify_password(username, password)
    elif grant_type == 'wxapp':
        account = verify_wxapp(username, password)
    if not account:
        return {}
    payload = {
        "iss": "gusibi.com",
         "iat": int(time.time()),
         "exp": int(time.time()) + 86400 * 7,
         "aud": "www.gusibi.com",
         "sub": account['_id'],
         "username": account['username'],
         "scopes": ['open']
    }
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    return True, {'access_token': token, 'account_id': account['_id']}
    

def verify_bearer_token(token):
    #  如果在生成token的时候使用了aud参数，那么校验的时候也需要添加此参数
    payload = jwt.decode(token, 'secret', audience='www.gusibi.com', algorithms=['HS256'])
    if payload:
        return True, token
    return False, token
	