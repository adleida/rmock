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

def main():


    import rmock
    parse = argparse.ArgumentParser(description='rmock')
    parse.add_argument('-v', '--version', action='version', version=rmock.__version__)
    ps = parse.parse_args()


    cfg = load_resource('rmock.yaml') 
    host, port = cfg.get('rmock', '0.0.0.0:6001').split(':')
    debug = cfg.get('debug',  True)
    rmock = Rmock()
    rmock.run(host=host, port=int(port), debug=debug)


if __name__ == '__main__':
    main()
