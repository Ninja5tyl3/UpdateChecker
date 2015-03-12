#!/usr/bin/env python3

import json

__author__ = 'jacob'


def configreader():

    json_data = open('config.json')

    config = json.load(json_data)

    json_data.close()

    return config


def configwriter(config):

    # with open('config.json', 'w') as configfile:
    #    config.write(configfile)

    json.dump(config, 'config.json')

    return


def configdefaults(config):

    config['compression'] = 'zip'
    config['url']['ninjaconfigs'] = 'https://raw.githubusercontent.com/Ninja5tyl3/Version/master/NinjaConfigs.json'
    config['url']['updatechecker'] = 'https://raw.githubusercontent.com/Ninja5tyl3/Version/master/UpdateChecker.json'
    config['version']['ninjaconfigs'] = '0.0.0'
    config['version']['updatechecker'] = '0.0.0'

    with open('config.conf', 'w') as configfile:
        config.write(configfile)

    return
