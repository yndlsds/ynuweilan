# -*- coding: utf-8 -*-
from flask import request, url_for
from mysite import db#, mc
from mysite.models import User, Weixin
from . import weixin
from ._verification import verification
from ._receive import is_subscribe_event, is_unsubscribe_event, is_text_msg
from ._response import parse_msg, response_text_msg, response_news_msg 
from .message import welcome_text, help_text, not_find_text, disease_text, symptom_text

@weixin.route("/<path:weixinhao>", methods = ["POST"])
def forward(weixinhao):
    weixin = Weixin.query.filter_by(name=weixinhao).first_or_404() 
    if verification(request, weixin.random):
        msg = parse_msg(request.data)
        openid = msg["FromUserName"]

        if is_subscribe_event(msg):
            user = User.query.filter(db.and_(User.weixinhao==weixinhao, User.openid==openid)).first()
            if user:
                user.state = True
            else:
                user = User(weixinhao=weixinhao, openid=openid)
            db.session.add(user)
            db.session.commit()
            return response_text_msg(openid, weixinhao, welcome_text)

        if is_unsubscribe_event(msg):
            user = User.query.filter(db.and_(User.weixinhao==weixinhao, User.openid==openid)).first_or_404()
            user.state = False
            db.session.add(user)
            db.session.commit()

        if is_text_msg(msg):
            content = msg["Content"]

            #request for help            
            if content[0] == u"?" or content[0] == u"？ ":
                return response_text_msg(openid, weixinhao, help_text)

            #request for login
            if content[0] == u"#":
                random = msg["Content"][1:]
                # if random in mc:
                #     mc[random] = openid
                #     return response_text_msg(openid, weixinhao, u"登陆验证成功")
                # else:
                #     return response_text_msg(openid, weixinhao, u"未知随机码")

            # #request for disease
            # if content[0:2] == u"疾病" or content[0] == u"j" or content[0] == u"J":
            #     if u" " in content:
            #         diseases = []
            #         disease = Disease.query.filter_by(name=content.split(" ")[1]).first()
            #         if disease:
            #             diseases.append(disease)
            #         else:
            #             diseases = Disease.query.filter(Disease.name.like("%"+content.split(" ")[1]+"%")).limit(10).all()
            #         items = []
            #         if diseases:
            #             for disease in diseases:
            #                 items.append({
            #                     "title": disease.name,
            #                     "description": disease_text % (disease.name, disease.people, disease.bodypart, disease.symptom, disease.department),
            #                     "url": "http://xianglian.sinaapp.com" + url_for("disease.detail", diseaseId=disease.id)
            #                 })                       
            #             return response_news_msg(openid, weixinhao, items)
            #         else:
            #             return response_text_msg(openid, weixinhao, not_find_text)
            #     else:
            #         return response_text_msg(openid, weixinhao, help_text)
            
            return response_text_msg(openid, weixinhao, help_text)

        return response_text_msg(openid, weixinhao, help_text)
    return "message processing fail"