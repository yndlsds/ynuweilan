import urllib, urllib2

UPLOAD_URL = "http://file.api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s"
GET_URL = "http://file.api.weixin.qq.com/cgi-bin/media/get?access_token=%s&media_id=%s"

def upload_media(access_token, media_type, media):
    req = urllib2.Request(UPLOAD_URL % (access_token, media_type), urllib.urlencode(media))
    response = urllib2.urlopen(req)
    return response.read()

def get_media(access_token, media_id):
    response = urllib2.urlopen(UPLOAD_URL % (access_token, media_id))
    return response.read()