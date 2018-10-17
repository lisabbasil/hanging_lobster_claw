#!/usr/bin/env python3

""" Master window module for project Alperose. """

from tkinter import Tk, Label, Button, Frame
from collections import OrderedDict
from logger import logging
from DataAccess import DataAccess


class MasterWin:

    """ Master window for project Alperose. """

    def __init__(self, master):
        self.master = master
        master.title('Super Mario Control Center')

        # Read data from json file
        logging.debug('Read data from json')
        self._data = read_data()

        # Define plants, subsystems and informations
        self._plants = OrderedDict({'moms': ['Mamis', self._moms],
                                    'shoots': ['Steckis', self._shoots],
                                    'veg': ['Vegi', self._veg],
                                    'buds': ['Buds', self._buds]})
        self._subsystems = \
            OrderedDict({'system': 'System', 'maintenance': 'Wartung', 'lamp':
                         'Lampe', 'fan': 'Lueftung', 'pump': 'Pumpe'})
        self._informations = \
            OrderedDict({'runtime': 'System laeuft seit', 'waterexchange':
                         'Letzter Wasserwechsel', 'tempair': 'Lufttemperatur',
                         'tempwater': 'Wassertemperatur'})

        # Set up all labels, buttons and indicators
        logging.debug('Set up labels')
        self.labels()
        logging.debug('Set up buttons')
        self.buttons()
        logging.debug('Set up indicators')
        self.indicators()

    def labels(self):

        """ Initialize and place all labels in master window. """

        width = 25
        height = 2

        # Dictionary storing all labels
        self._d_labels = {}
        self._d_labels['title'] = Label(self.master,
                                        text='Super Mario Control Center',
                                        height=height)
        for skey, sval in self._subsystems.items():
            self._d_labels[skey] = Label(self.master, text=sval,
                                         width=width, height=height)
        for ikey, ival in self._informations.items():
            self._d_labels[ikey] = Label(self.master, text=ival,
                                         width=width, height=height)

        # Positioning of labels
        self._d_labels['title'].grid(row=0, column=0, columnspan=5)
        for sidx, skey in enumerate(self._subsystems):
            self._d_labels[skey].grid(row=sidx+2, column=0)
        for iidx, ikey in enumerate(self._informations):
            self._d_labels[ikey].grid(row=iidx+2+len(self._subsystems),
                                      column=0)

    def buttons(self):

        """ Initialize and place all buttons in master window. """

        width = 15
        height = 3

        # Dictionary storing all buttons
        self._d_buttons = {}
        for pkey, pval in self._plants.items():
            self._d_buttons[pkey] = \
                Button(self.master, text=pval[0], command=pval[1], width=width,
                       height=height)

        # Positioning of buttons
        for pidx, pkey in enumerate(self._plants):
            self._d_buttons[pkey].grid(row=1, column=pidx+1)

    def indicators(self):

        """ Initialize and place all indicators in master window. Indicators
        typically show if a system is on or off. """

        width = 15
        height = 2

        # Dictionary storing all indicators
        self._d_indicators = {}
        for pkey in self._plants:
            for skey in self._subsystems:
                gkey = get_global_key([pkey, skey])
                self._d_indicators[gkey] = \
                    Label(self.master,
                          text=on_off_text(self._data[pkey][skey]),
                          width=width, height=height,
                          bg=on_off_bg(self._data[pkey][skey]))

        # Positioning of indicators
        for pidx, pkey in enumerate(self._plants):
            for sidx, skey in enumerate(self._subsystems):
                gkey = get_global_key([pkey, skey])
                self._d_indicators[gkey].grid(row=sidx+2, column=pidx+1)

    def _moms(self):

        """ Method called when pressing the moms button. """

        test = Tk()

        pkey = 'moms'

        width = 25
        height = 2

        self._d_moms = {}

        # Adding horizontal line
        self._d_moms['hr'] = Frame(self.master, height=2,width=500,bg="black")
        self._d_moms['hr'].grid(row=99, column=0, columnspan=5)

        # Adding content at the bottom
        self._d_moms[get_global_key([pkey, 'title'])] = \
            Label(test, text='Mamis', height=height)
        for skey, sval in self._subsystems.items():
            self._d_moms[get_global_key([pkey, skey])] = \
                Label(test, text=sval, width=width, height=height)

        # Positioning of labels
        self._d_moms[get_global_key([pkey, 'title'])].\
            grid(row=100, column=0, columnspan=5)
        for sidx, skey in enumerate(self._subsystems):
            self._d_moms[get_global_key([pkey, skey])].\
                grid(row=sidx+102, column=0)

        width = 15
        height = 2

        # Dictionary storing all indicators
        for skey in self._subsystems:
            gkey = get_global_key([pkey, skey])
            self._d_moms[gkey] = \
                Button(test,
                       text=on_off_text(self._data[pkey][skey]),
                       width=width, height=height,
                       bg=on_off_bg(self._data[pkey][skey]))

        # Positioning of indicators
        for sidx, skey in enumerate(self._subsystems):
            gkey = get_global_key([pkey, skey])
            self._d_moms[gkey].grid(row=sidx+102, column=1)

    def _shoots(self):

        """ Method called when pressing the shoots button. """

        print('Inside function shoots()')

    def _veg(self):

        """ Method called when pressing the veg button. """

        print('Inside function veg()')

    def _buds(self):

        """ Method called when pressing the buds button. """

        print('Inside function buds()')


def read_data():

    """ Method to read data from json file. """

    return DataAccess('data.json').read()


def on_off_text(n):

    """ Returns OFF, when n=0, ON otherwise. """

    return 'OFF' if n == 0 else 'ON'


def on_off_bg(n):

    """ Return bg colors for off/on. """

    return '#D00000' if n == 0 else '#248232'


def get_global_key(l):

    """ Return global key formed from a list of keys. """

    return '_'.join([str(x) for x in l])
