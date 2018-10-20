#!/usr/bin/env python3

""" Module to read and write json data from project Alperose. """

from json import load
from logger import logging
from pprint import pformat


class DataAccess:

    """ Class that provides read and write functions to access json data. """

    def __init__(self, filename):
        self._filename = filename
        logging.info('Initialize DataAccess object for reading json file %s' %
                      filename)

    def read(self):

        """ Read from json file. """

        logging.info('Read json data from %s' % self._filename)
        with open(self._filename) as json:
            data = load(json)

        # Use pprint to format json data nicely
        logging.info('Retrieve json data:')
        logging.info(pformat(data))
        return data

    def write(self):

        """ Write to json file. """

        pass
