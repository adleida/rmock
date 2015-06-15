#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time
import uuid
import os
import rmock
import logging
from . utils import compare_dictionaries, load_resource
from flask import request, jsonify, abort, current_app as app

logger = logging.getLogger(__name__)
adm = load_resource('creative.yaml')


def index():

    return jsonify({
        "Rmock": "Welcome to rmock dsp",
        "version": rmock.__version__,
        "timestamp": time.time()
    })


def post_conf():

    if request.json and request.json.get('dsp', {}):
        app.conf = request.json.get('dsp')
        uid = uuid.uuid4()
        logging.info('uuid = %s ' % uid)
        logging.info('conf = %s ' % app.conf)
        return jsonify({"conf": True, "uuid": uid})
    return jsonify({"conf": False})


def check_conf():

    return jsonify(app.conf)


def return_dsp():

    tmp = app.conf.get('s', [])
    res = [{'name': it['name'], 'burl': it['burl'], 'id': it['id']} for it in tmp]
    td = app.json_dump(res)
    logging.info('dsp_info >>> %s' % td)
    return td


def return_res(did):

    logging.info('bid_request >>> %s' % app.json_dump(request.json))
    tmp = app.conf.get('s', [])
    tt = [(it['id'], it.get('res_file', {}), it['is_res'], it['name'], it.get('notice_file', {})) for it in tmp]
    for l in tt:
        if l[0] == did:
            if l[2]:
                res_data = l[1]
                try:
                    if res_data.get("id", ""):
                        logging.info('bid_request_id >>> %s' % res_data['id'])
                        logging.info('bid_response >>> %s' % app.json_dump(res_data))
                        return jsonify(res_data)
                    res_data['id'] = request.json['id']
                    return jsonify(res_data)
                except Exception as ex:
                    logging.error('Error %s ' % ex)
                    return jsonify(res_data)
            else:
                time.sleep(2)
    abort(404)


def get_notice(did):

    tmp = app.conf.get('s', [])
    tt = [(it['id'], it.get('res_file', {}), it['is_res'], it['name'], it.get('notice_file', {})) for it in tmp]
    logging.info('bid_notice >>> %s' % app.json_dump(request.json))
    for i in tt:
        if did == i[0]:
            try:
                data_json = i[4]
                request.json.pop('id')
                compare_dictionaries(request.json, data_json)
                app.notice_win = True
                logging.info('notice: True')
            except Exception as ex:
                app.notice_win = False
                logging.error('notice: False')
                print(ex)
        continue
    res_notice = {"message": "{} get notice".format(did), "time": time.time()}
    logging.info('response_notice >>> %s' % app.json_dump(res_notice))
    return jsonify(res_notice)


def return_adm(mid):
    for item in adm:
        if mid == item['id']:
            logging.info('mid: %s' % mid)
            return jsonify(item)
    logging.error('adm not found')
    abort(404)


def random_dsp():
    pass
