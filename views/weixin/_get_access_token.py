import urllib2

def get_access_token(appid, appsecret):
    url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % appid, appsecret
    response = urllib2.urlopen(url)
    data = json.load(response) 
    return data.access_token