#!/usr/bin/env python3

import os
import shutil
import sys

__author__ = 'jacob'


class ProgressBar(object):
    def __init__(self, message, width=20, progressSymbol=u'▣ ', emptySymbol=u'□ '):
        self.width = width

        if self.width < 0:
            self.width = 0

        self.message = message
        self.progressSymbol = progressSymbol
        self.emptySymbol = emptySymbol

    def update(self, progress):
        totalBlocks = self.width
        filledBlocks = int(round(progress / (100 / float(totalBlocks))))
        emptyBlocks = totalBlocks - filledBlocks

        progressBar = self.progressSymbol * filledBlocks + \
                      self.emptySymbol * emptyBlocks

        if not self.message:
            self.message = u''

        progressMessage = u'\r{0} {1}  {2}%'.format(self.message,progressBar,progress)

        sys.stdout.write(progressMessage)
        sys.stdout.flush()

    def calculateAndUpdate(self, done, total):
        progress = int(round( (done / float(total)) * 100))
        self.update(progress)


def countFiles(directory):
    files = []

    if os.path.isdir(directory):
        for path, dirs, filenames in os.walk(directory):
            files.extend(filenames)

    return len(files)


p = ProgressBar('Copying files...')


def makedirs(dest):
    if not os.path.exists(dest):
        os.makedirs(dest)


def copyFilesWithProgress(src, dest):
    numFiles = countFiles(src)

    if numFiles > 0:
        makedirs(dest)

        numCopied = 0

        for path, dirs, filenames in os.walk(src):
            for directory in dirs:
                destDir = path.replace(src, dest)
                makedirs(os.path.join(destDir, directory))

            for sfile in filenames:
                srcFile = os.path.join(path, sfile)

                destFile = os.path.join(path.replace(src, dest), sfile)

                shutil.copy(srcFile, destFile)

                numCopied += 1

                p.calculateAndUpdate(numCopied, numFiles)

        print