#!/usr/bin/env python
#
# Logging
#
import os
import logging
import logging.handlers

DEBUG = logging.DEBUG
INFO  = logging.INFO
WARN  = logging.WARN
ERROR = logging.ERROR


class NullHandler(logging.Handler):
    def emit(self, record):
        pass


def mkdirp(directory):
    if not os.path.isdir(directory):
        os.makedirs(directory)


def setupLogging(name):
    #
    # Logging setup
    #
    mkdirp(u"logs")
    logger = logging.getLogger(name)
    logFile = u'./logs/log.txt'

    # Note: Levels - DEBUG INFO WARN ERROR CRITICAL
    logger.setLevel(logging.INFO)

    logFormatter = logging.Formatter(u"%(asctime)s [%(levelname)-5.5s] [%(filename)s:%(lineno)s ] %(message)s")

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    logger.addHandler(consoleHandler)

    fileHandler = logging.handlers.RotatingFileHandler(logFile, maxBytes=10485760, backupCount=5)
    fileHandler.setFormatter(logFormatter)
    logger.addHandler(fileHandler)

    h = NullHandler()
    logger.addHandler(h)

    return logger


