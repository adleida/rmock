#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from termcolor import colored
import json
import os
import yaml
import io
import pkgutil
import functools
import logging


class MyError(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "The error message is %s" % self.message


def compare_dictionaries(dict1, dict2):

    '''cmp dict'''
    dicts_are_equal = True
    for key in dict2.keys():
        if type(dict2[key]) is dict:
            dicts_are_equal = dicts_are_equal and compare_dictionaries(dict1[key], dict2[key])
        else:
            dicts_are_equal = dicts_are_equal and (dict1[key] == dict2[key])
            if not dicts_are_equal:
                raise MyError("The key %s of dict1 not equeal dict2" % key)

    return dicts_are_equal


def color(msg, clr):
    print(colored(unicode(clr), clr))


def set_log(logger, fname):
    fm = logging.Formatter("""%(asctime)s:[%(filename)s:%(lineno)d]:%(message)s""")
    fn = logging.FileHandler('./log/' + str(fname), mode='w')
    logger.handler = []
    fn.setLevel(logging.ERROR)
    fn.setFormatter(fm)
    logger.addHandler(fn)


def json_dump(data):
    return json.dumps(data, indent=2)


@functools.lru_cache()
def load_resource(name, as_object=True):

    path = 'res/{}'.format(name)
    blob = pkgutil.get_data(__package__, path)
    if blob == None:
        raise Exception('no such resource: {}'.format(name))
    data = blob.decode()
    if as_object:
        ext = os.path.splitext(name)[-1]
        if ext in ['.json']:
            data = json.loads(data)
        elif ext in ['.yaml', '.yml']:
            data = yaml.load(io.StringIO(data))
        else:
            raise Exception('cannot detect resource type')
    return data

