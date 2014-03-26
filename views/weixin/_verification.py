import hashlib

def verification(request, token):
    signature = request.args.get("signature")
    timestamp = request.args.get("timestamp")
    nonce = request.args.get("nonce")
    tmplist = [token, timestamp, nonce]
    tmplist.sort()
    tmpstr = "".join(tmplist)
    hashstr = hashlib.sha1(tmpstr).hexdigest()
    if hashstr == signature:
        return True
    return False    