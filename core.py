#!/usr/bin/env python3

import updater
from walker import walker
from copywprogress import makedirs
import jsonparser
import configuration

import configparser

__author__ = 'jacob'


def configreader():

    config = configparser.ConfigParser()
    config.read('config.conf')

    return config


def configwriter(config):

    # config = configreader()

    with open('config.conf', 'w') as configfile:
        config.write(configfile)

    return


def configdefaults():

    config = configreader()

    config['config']['compression'] = 'zip'
    config['config']['ninjaconfigs'] = 'https://raw.githubusercontent.com/Ninja5tyl3/Version/master/NinjaConfigs.json'
    config['config']['updatechecker'] = 'https://raw.githubusercontent.com/Ninja5tyl3/Version/master/UpdateChecker.json'

    with open('config.conf', 'w') as configfile:
        config.write(configfile)

    return


def core():

    makedirs('tmp')

    makedirs('data')

    # updater()

    print(updater.md5sum('.gitignore'))

    # print(config['version']['ninjaconfigs'])

    # print(updater.md5sum('data/NinjaConfigs.json'))

    # updater.checker()

    jsonparser.updatecheckerninjaconfigs()

    config = configreader()

    print(config['version']['ninjaconfigs'])

    newconfig = configuration.configreader()

    print(newconfig['version']['ninjaconfigs'])

    # tar()

    # urlretrieve('https://github.com/Ninja5tyl3/NinjaConfigs/archive/master.zip', 'tmp/NinjaConfigs.zip')

    # copyFilesWithProgress('/tmp/NinjaConfigs-master', '../minecraft')
    # shutil.rmtree('tmp', True)

    # configwriter()

    # print(config['config']['compression'])

    return