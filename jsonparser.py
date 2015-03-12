#!/usr/bin/env python3

import json
import hashlib
import core
from urllib.request import urlretrieve
import configuration


__author__ = 'jacob'


def updatecheckerninjaconfigs():

    json_data = open('data/NinjaConfigs.json')

    data = json.load(json_data)
    # pprint(data)

    newversion = data['tag_name']

    config = configuration.configreader()

    oldversion = config['version']['ninjaconfigs']

    print(newversion)

    print(oldversion)

    if newversion <= oldversion:
        print('No new updates')
    else:
        print('New Updates are Available!')
        config['version']['ninjaconfigs'] = newversion

    print(config['version']['ninjaconfigs'])

    configuration.configwriter(config)


def jsonupdater(program):

    config = core.configreader()

    link = config['config'][program]

    file = program + '.json'

    urlretrieve(link, file)


def updater(file):

    json_data = open(file + '.json')

    data = json.load(json_data)
    pprint(data)

    htmlurl = data['html_url']

    targzdl = htmlurl + '.tar.gz'

    zipdl = htmlurl + '.zip'

    print(zipdl)

    # pprint(tarball)

    # urlretrieve(tarball, 'configs.tar.gz')

    # urlretrieve(browserdownload, 'confgs.zip')

    json_data.close()