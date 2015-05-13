#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time
import uuid
import os
import rmock
from . utils import compare_dictionaries, load_resource, set_log
from flask import request, jsonify, abort, current_app as app


def index():

    return jsonify({
        "Rmock": "Welcome to rmock dsp",
        "version": rmock.__version__,
        "timestamp": time.time()
    })


def post_conf():
    log_path = os.path.join(app.root_path, 'log') 
    if request.json and request.json.get('dsp', {}):
        app.conf = request.json.get('dsp')
        uid = uuid.uuid4()
        set_log(app.logger, uid)
        app.logger.info('uuid = %s ' % uid)
        app.logger.info('conf = %s ' % app.conf)
        return jsonify({"conf": True, "uuid": uid})
    return jsonify({"conf": False})


def check_conf():

    return jsonify(app.conf)


def return_dsp():

    tmp = app.conf.get('s', [])
    res = [{'name': it['name'], 'burl': it['burl'], 'id': it['id']} for it in tmp]
    td = app.json_dump(res)
    app.logger.info('dsp_info >>> %s' % td)
    return td



def return_res(did):

    app.logger.info('bid_request >>> %s' % app.json_dump(request.json))
    tmp = app.conf.get('s', [])
    tt = [(it['id'], it.get('res_file', {}), it['is_res'], it['name'], it.get('notice_file', {})) for it in tmp]
    for l in tt:
        if l[0] == did:
            if l[2]:
                res_data = l[1]
                rid = res_data.get('id', '')
                if not rid:
                    res_data['id'] = request.json['id']
                app.logger.info('bid_response >>> %s' % app.json_dump(res_data))
                return jsonify(res_data)
            else:
                time.sleep(2)
    abort(404)


def get_notice(did):

    tmp = app.conf.get('s', [])
    tt = [(it['id'], it.get('res_file', {}), it['is_res'], it['name'], it.get('notice_file', {})) for it in tmp]
    app.logger.info('bid_notice >>> %s' % app.json_dump(request.json))
    for i in tt:
        if did == i[0]:
            try:
                data_json = i[4]
                request.json.pop('id')
                compare_dictionaries(request.json, data_json)
                app.notice_win = True
            except Exception as ex:
                app.notice_win = False
                print(ex)
        continue
    res_notice = {"message": "{} get notice".format(did), "time": time.time()}
    app.logger.info('response_notice >>> %s' % app.json_dump(res_notice))
    return jsonify(res_notice)


def return_adm(mid):

    adm = load_resource('creative.yaml')
    for item in adm:
        if mid == item['id']:
            return jsonify(item)
    abort(404)


def random_dsp():
    pass
