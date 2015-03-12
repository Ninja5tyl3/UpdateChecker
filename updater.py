#!/usr/bin/env python3

from urllib.request import urlretrieve
from functools import partial
import core
import hashlib


__author__ = 'jacob'


def md5sum(filename):
    with open(filename, mode='rb') as f:
        d = hashlib.md5()
        for buf in iter(partial(f.read, 128), b''):
            d.update(buf)
    return d.hexdigest()


def checker():

    config = core.configreader()

    if config['hash']['ninjaconfigs'] == '':
        confighash = md5sum('NinjaConfigs.json')
    else:
        confighash = config['hash']['ninjaconfigs']

    if config['hash']['updatechecker'] == '':
        updatehash = md5sum('UpdateChecker.json')
    else:
        updatehash = config['hash']['updatechecker']

    configsnew = config['config']['ninjaconfigs']

    urlretrieve(configsnew, 'tmp/NinjaConfigs.json')

    updatenew = config['config']['updatechecker']

    urlretrieve(updatenew, 'tmp/UpdateChecker.json')

    configsnewhash = str(md5sum('tmp/NinjaConfigs.json'))

    updatenewhash = str(md5sum('tmp/UpdateChecker.json'))

    if confighash != configsnewhash:
        config.set('hash', 'ninjaconfigs', configsnewhash)
        print('New Update Available')
    else:
        print('No New Updates')

    if updatehash != updatenewhash:
        config.set('hash', 'updatechecker', updatenewhash)
        print('New Update Available')
    else:
        print('No New Updates')

    return




def updater():

    config = core.configreader()

    ninjaconfigs = config['config']['ninjaconfigs']

    updatechecker = config['config']['updatechecker']

    print(config['config']['ninjaconfigs'])

    # request.urlretrieve(ninjaconfigs, 'tmp/NinjaConfigs.json')

    # urlretrieve(updatechecker, 'tmp/UpdateChecker.json')

    return