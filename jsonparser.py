#!/usr/bin/env python3

import json
import hashlib
import core
from urllib.request import urlretrieve


__author__ = 'jacob'


def updatechecker(program):

    json_data = open('data/' + program + '.json')

    data = json.load(json_data)
    # pprint(data)

    newversion = data['tag_name']

    config = core.configreader()

    oldversion = config['version'][program]

    if newversion <= oldversion:
        print('No new updates')
    else:
        print('New Updates are Available!')
        config['version'][program] = newversion


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