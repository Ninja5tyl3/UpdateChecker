#!/usr/bin/env python3

import tarfile
import zipfile

__author__ = 'jacob'


def tar():

    t = tarfile.open('configs.zip', 'r')
    # t.extractall()
    # t.extract('Configs/*', 'tmp')
    t.close()

    return