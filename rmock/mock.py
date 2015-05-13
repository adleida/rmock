#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# File Name: mock.py
# Author: fanyongtao
# mail: jacketfan826@gmail.com
# Created Time: 2015年05月11日 星期一 15时33分20秒
#########################################################################
from .flaskapp import Rmock
from .utils import load_resource
from .endpoints import index
import argparse
import logging
import logging.config

def main():


    import rmock
    parse = argparse.ArgumentParser(description='rmock')
    parse.add_argument('-v', '--version', action='version', version=rmock.__version__)
    parse.add_argument('-p', '--port', dest='port', type=int, default=6001)
    ps = parse.parse_args()

    cfg = load_resource('rmock.yaml') 
    log = cfg.get('logging', {})
    log.setdefault('version', 1)
    logging.config.dictConfig(log)

    host = cfg.get('rmock', '0.0.0.0')
    debug = cfg.get('debug',  False)

    rmock = Rmock()
    rmock.run(host=host, port=int(ps.port), debug=debug)


if __name__ == '__main__':

    main()
