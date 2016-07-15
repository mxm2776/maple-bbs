#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: urls.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-07-15 18:12:22 (CST)
# Last Update:星期五 2016-7-15 20:20:11 (CST)
#          By:
# Description:
# **************************************************************************
from flask import Blueprint
from .views import ask, good, preview, vote_up, vote_down
from .views import TopicAPI, ReplyAPI

site = Blueprint('topic', __name__)

site.add_url_rule('/ask', view_func=ask)
site.add_url_rule('/good', view_func=good)
site.add_url_rule('/preview', view_func=preview, methods=['POST'])
site.add_url_rule('/up/<topicId>', view_func=vote_up, methods=['POST'])
site.add_url_rule('/down/<topicId>', view_func=vote_down, methods=['POST'])

topic_view = TopicAPI.as_view('topic')
# /topic
# /topic         post
# /topic/<uid>   get,put,delete
site.add_url_rule('',
                  defaults={'uid': None},
                  view_func=topic_view,
                  methods=['GET'])
site.add_url_rule('', view_func=TopicAPI.as_view('post'), methods=['POST'])
site.add_url_rule('/<uid>',
                  view_func=topic_view,
                  methods=['GET', 'PUT', 'DELETE'])

reply_view = ReplyAPI.as_view('reply')
site.add_url_rule('/<topicId>/reply', view_func=reply_view, methods=['POST'])
