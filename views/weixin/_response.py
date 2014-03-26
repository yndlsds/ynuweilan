from xml.etree import ElementTree
import time
from flask import make_response

#format msg to dict
def parse_msg(rawmsgstr):
    root = ElementTree.fromstring(rawmsgstr)
    msg = {}
    for child in root:
       msg[child.tag] = child.text
    return msg

#response message
def response_text_msg(openid, weixinhao, content):
    response = make_response(TEXT_MSG % (openid, weixinhao, str(int(time.time())), content))
    response.content_type = "application/xml"
    return response

def response_voice_msg(openid, weixinhao, content):
    response = make_response(VOICE_MSG % (openid, weixinhao, str(int(time.time())), content))
    response.content_type = "application/xml"
    return response

def response_news_msg(openid, weixinhao, items):
    header = NEWS_MSG_HEADER % (openid, weixinhao, str(int(time.time())), len(items))
    body = ""
    for item in items:
        body += NEWS_MSG_BODY % (item["title"], item["description"], item["url"])
    footer = NEWS_MSG_FOOTER
    response = make_response(header+body+footer)
    response.content_type = "application/xml"
    return response

#-- weixin xml --
TEXT_MSG = \
"""
<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>%s</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[%s]]></Content>
</xml>
"""

VOICE_MSG = \
"""
<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>%s</CreateTime>
<MsgType><![CDATA[voice]]></MsgType>
<Voice>
<MediaId><![CDATA[%s]]></MediaId>
</Voice>
</xml>
"""

NEWS_MSG_HEADER = \
"""
<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>%s</CreateTime>
<MsgType><![CDATA[news]]></MsgType>
<ArticleCount>%d</ArticleCount>
<Articles>
"""

NEWS_MSG_BODY = \
"""
<item>
<Title><![CDATA[%s]]></Title>
<Description><![CDATA[%s]]></Description>
<Url><![CDATA[%s]]></Url>
</item>
"""

NEWS_MSG_FOOTER = \
"""
</Articles>
</xml>
"""