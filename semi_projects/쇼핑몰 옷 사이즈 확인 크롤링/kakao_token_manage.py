from os import access
import requests
import json
import sys
import datetime

rest_API_key = '03e461ff4bab0a5e4979c7d12a3f6706'
redirect_uri = 'https://localhost.com/auth'
code = "m6zXqc2cg2ZNP31NTHprNcPevx-OSBK23UrTV1rUDXMMKuwJph5Wk_Vc4E_yLZoTh9Q0DAo9dNoAAAF7kcTTNQ"

# ------------------- 인증코드 받기 ---------------------#
# 인증 코드 받는 곳: https://kauth.kakao.com/oauth/authorize?client_id=03e461ff4bab0a5e4979c7d12a3f6706&redirect_uri=https://localhost.com/auth&response_type=code&scope=talk_message,friends

def registerAccessToken():
    url = 'https://kauth.kakao.com/oauth/token'
    data = {
        'grant_type': 'authorization_code',
        'client_id': rest_API_key,
        'redirect_uri': redirect_uri,
        'code': code
    }

    response = requests.post(url, data=data)
    tokens = response.json()

    with open("kakao_code.json", 'w') as fp:
        json.dump(tokens, fp)
    return(tokens)

def sendMessageToMe(message):
    temp = open("kakao_code.json", 'r')
    tokens = json.load(temp)
    current_time = "현재 시간 " + str(datetime.datetime.now())[:-7] + ".\n" + message

    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    headers = {
        "Authorization" : "Bearer " + tokens['access_token']
    }
    data = {
        "template_object" : json.dumps({
            "object_type" : "text",
            "text" : current_time,
            "link" : {
                "web_url" : "www.naver.com"
            }
        })
    }
    response = requests.post(url, headers=headers, data=data)
    return response.status_code

def sendMessageToFriend():
    url = "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"
    temp = open("kakao_code.json", 'r')
    tokens = json.load(temp)
    
    header = {"Authorization": 'Bearer ' + tokens['access_token']}
    uuid = ["itsem0@daum.net"]
    uuidsData = {"itsem0@daum.net" : json.dumps(uuid)}    
    
    post = {
        "object_type": "text",
        "text" : "보내고자 하는 TEXT",
        "link" : {
            "web_url" : "http://naver.com",
            "mobile_web_url" : "http://naver.com"
        },
        "button_title":"button title"
    }
    data = {"template_object": json.dumps(post)}
    uuidsData.update(data)

    return requests.post(url, headers=header, data=uuidsData).status_code

def refreshToken():
    url = "https://kapi.kakao.com/oauth/token"
    temp = open("kakao_code.json", 'r')
    tokens = json.load(temp)
    if 'refresh_token' not in tokens:
        return 'No token available'
    
    data = {
        "grant_type": "refresh_token",
        "client_id": rest_API_key,
        "refresh_token": tokens['refresh_token']
    }

    response = requests.post(url, data=data)
    tokens = response.json()
    
    with open("kakao_code.json", "w") as fp:
        json.dump(tokens, fp)
    return response.status_code, tokens, response.json()

# def checkTokenInfo():
#     url = "https://kapi.kakao.com/v1/user/access_token_info"

#     header = {
#         "Authorization" : "Bearer " + access_token
#     }

#     data = {
#         "id": 1869145849,
#         "expires_in": 21599,
#         "app_id": 629544
#     }
#     response = requests.post(url, data=data)
#     tokens = response.json()
#     return tokens