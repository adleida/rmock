#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time
import uuid
from . utils import set_log, compare_dictionaries
from flask import Flask, request, jsonify, current_app as app


def index():

    return jsonify({
        "Rmock": "Welcome to rmock dsp",
        "version": "0.0.2",
        "timestamp": time.time()
    })



def cfg():
    if request.json and request.json.get('dsp', {}):
        app.conf = request.json.get('dsp')
        uid = uuid.uuid4()
        set_log(app.logger, uid)
        app.logger.info('uuid = %s ' % uid)
        app.logger.info('conf = %s ' % app.conf)
        return jsonify({
            "conf": True,
            "uuid": uid
        })
    return jsonify({"conf": False})



def chk():
    return jsonify(app.conf)



def dsp():
    tmp = app.conf.get('s', [])
    res = [{
        'name': it['name'],
        'burl': it['burl'],
        'id': it['id']
    } for it in tmp]
    td = app.json_dump(res)
    app.logger.info('provide dsp info start'.center(40, '='))
    app.logger.info('dsp_info >>> %s' % td)
    app.logger.info('provide dsp info end'.center(40, '='))
    return td



def res(did):
    app.logger.info('====%s Get bid request start====' % did)
    app.logger.info('bid_request >>> %s' % app.json_dump(request.json))
    app.logger.info('====%s Get bid request end====' % did)
    tmp = app.conf.get('s', [])
    tt = [(it['id'], it.get('res_file', {}), it['is_res'], it['name'], it.get('notice_file', {})) for it in tmp]
    for l in tt:
        if l[0] == did:
            if l[2]:
                res_data = l[1]
                rid = res_data.get('id', '')
                if not rid:
                    res_data['id'] = request.json['id']
                app.logger.info('Response bid request start'.center(40, '='))
                app.logger.info('bid_response >>> %s' % app.json_dump(res_data))
                app.logger.info('Response bid request end'.center(40, '='))
                return jsonify(res_data)
            else:
                time.sleep(2)
    return jsonify({"j": "b"})



def notice(did):
    tmp = app.conf.get('s', [])
    tt = [(it['id'], it.get('res_file', {}), it['is_res'], it['name'], it.get('notice_file', {})) for it in tmp]
    app.logger.info('===%s Get bid notice start===' % did)
    app.logger.info('bid_notice >>> %s' % app.json_dump(request.json))
    app.logger.info('===%s Get bid notice end===' % did)
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
    res_notice = {
        "message": "{} get notice".format(did),
        "time": time.time()
    }
    app.logger.info('Response bid notice start'.center(40, '='))
    app.logger.info('response_notice >>> %s' % app.json_dump(res_notice))
    app.logger.info('Response bid notice end \n\n\n')
    return jsonify(res_notice)
