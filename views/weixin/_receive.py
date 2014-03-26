#weixin event
def is_subscribe_event(msg):
    return msg["MsgType"] == "event" and msg["Event"] == "subscribe"

def is_unsubscribe_event(msg):
    return msg["MsgType"] == "event" and msg["Event"] == "unsubscribe"

def is_location_event(msg):
    return msg["MsgType"] == "event" and msg["Event"] == "LOCATION"

#message type
def is_text_msg(msg):
    return msg["MsgType"] == "text"

def is_image_msg(msg):
    return msg["MsgType"] == "image"

def is_voice_msg(msg):
    return msg["MsgType"] == "voice"

def is_video_msg(msg):
    return msg["MsgType"] == "video"

def is_location_msg(msg):
    return msg["MsgType"] == "location"

def is_link_msg(msg):
    return msg["MsgType"] == "link"