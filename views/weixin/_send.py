import urllib, urllib2
from flask import make_response

SEND_URL = "https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=%s"

#send message
def send_msg(message, access_token):
    req = urllib2.Request(SEND_URL % access_token, urllib.urlencode(message))
    response = urllib2.urlopen(req)
    return response.read()

def send_text_msg(openid, content, access_token):
    message = {
        "touser":openid,
        "msgtype":"text",
        "text":{
             "content":content
        }
    }
    send_msg(message, access_token)

def send_voice_msg(openid, media_id, access_token):
    message = {
        "touser":openid,
        "msgtype":"voice",
        "text":{
            "media_id":media_id
        }
    }
    send_msg(message, access_token)

def send_news_msg(openid, Items, access_token):
    message = {
        "touser":openid,
        "msgtype":"news",
        "news":{
            "articles": items
        }
    }
    send_msg(message, access_token)

