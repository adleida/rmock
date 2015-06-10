#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# File Name: rmock/app.py
# Author: fanyongtao
# mail: jacketfan826@gmail.com
# Created Time: 2015年05月11日 星期一 16时03分37秒
#########################################################################
import os
import logging
import uuid
import time
import json
from . endpoints import (index, post_conf, return_adm, get_notice,
                         return_res, return_dsp, check_conf)
from flask import Flask, request, make_response, jsonify


class Rmock(Flask):

    def __init__(self, **kwargs):
        self.conf = {}
        name = kwargs.pop('name', __package__)
        super(Rmock, self).__init__(name, **kwargs)
        self.init()

    def run(self, host=None, port=None, debug=None, **kwargs):
        super(Rmock, self).run(host, port, debug, **kwargs)

    @staticmethod
    def json_dump(data):
        return json.dumps(data, indent=2)

    def init(self):
        self.add_url_rule('/', view_func=index, methods=["GET"])
        self.add_url_rule('/conf', view_func=post_conf, methods=["POST"])
        self.add_url_rule('/chk', view_func=check_conf, methods=["GET"])
        self.add_url_rule('/dsp/v2', view_func=return_dsp, methods=["GET"])
        self.add_url_rule('/res/v2/<string:did>', view_func=return_res, methods=["POST"])
        self.add_url_rule('/notice/v2/<string:did>', view_func=get_notice, methods=["POST"])
        self.add_url_rule('/adm/v2/<string:mid>', view_func=return_adm, methods=["GET"])
