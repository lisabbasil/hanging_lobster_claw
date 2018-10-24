#!/usr/bin/env python3

""" Master window module for project Alperose. """

from tkinter import Tk, Label, Button, Frame
from collections import OrderedDict
from logger import logging
from DataAccess import DataAccess
from actions import *

# TODO: Clean up with Syntastic
# TODO: Review all docstrings. Things are moving here!
# TODO: When creating elements and positioning them, you make the same loop
#       twice, should they be merged and done in one step?
# TODO: Currently, the json gets completely rewritten when a change occurs,
#       maybe it would be faster if only the change is written (likely doesn't
#       make a difference, though)
# TODO: Check if all the dictionaries (e.g. _d_labels) should be class
#       variables instead of object variables
# TODO: Currently you pass both arguments self.master and 'master' to the
#       indicators method. You could merge them by identifiying the window from
#       self.master only (e.g. by using a method like get_title() or
#       something).
# TODO: Using eval to call all the actions is evil.
# TODO: In the method _get_data(), if the key combination is not found in the
#       json file, an error is thrown. This means that a new key combination
#       can only be introduced by editing the json file by hand at first. It
#       might be better to throw a warning instead of an error, assume default
#       values for the unknown key combinations and store them in the json.
#       Next time it will be a known key combination.

def on_off_text(n):

    """ Returns OFF, when n=0, ON otherwise. """

    return 'OFF' if n == 0 else 'ON'


def on_off_bg(n):

    """ Return bg colors for off/on. """

    return '#D00000' if n == 0 else '#248232'


def get_global_key(l):

    """ Return global key formed from a list of keys. """

    return '_'.join([str(x) for x in l])


class MasterWin:

    """ Master window for project Alperose. """

    # Define plants, subsystems and informations
    #_plants = OrderedDict({'moms': 'Mamis', 'shoots': 'Steckis', 'veg': 'Vegi',
    #                       'buds': 'Buds'})
    #_plants = OrderedDict({'moms': 'Mamis', 'shoots': 'Steckis', 'veg': 'Vegi'})
    _plants = OrderedDict({'moms': 'Mamis', 'shoots': 'Steckis'})
    #_subsystems = \
    #    OrderedDict({'system': 'System', 'maintenance': 'Wartung', 'lamp':
    #                 'Lampe', 'fan': 'Lueftung', 'pump': 'Pumpe'})
    _subsystems = \
        OrderedDict({'system': 'System', 'lamp2': 'Lampe'})
    _informations = \
        OrderedDict({'runtime': 'System laeuft seit', 'waterexchange':
                     'Letzter Wasserwechsel', 'tempair': 'Lufttemperatur',
                     'tempwater': 'Wassertemperatur'})

    # Read data from json file
    logging.info('Read data from json')
    _jsonobject = DataAccess('data.json')
    _data = _jsonobject.read()

    # Dictionaries storing all the Tkinter objects
    _d_indicators = {}

    def __init__(self, master):
        self.master = master
        master.title('Super Mario Control Center')

        # Set up all labels, buttons and indicators in master window
        logging.info('Set up labels in window master')
        self.labels(self.master, 'Super Mario Control Center')
        logging.info('Set up buttons in window master')
        self.buttons(self.master)
        logging.info('Set up indicators in window master')
        self.indicators(self.master, 'master')

    def labels(self, window, title=''):

        """ Initialize and place all labels in window. """

        width = 25
        height = 2

        # Dictionary storing all labels
        self._d_labels = {}
        self._d_labels['title'] = Label(window, font=(24),
                                        text=title,
                                        height=4)
        for skey, sval in self._subsystems.items():
            self._d_labels[skey] = Label(window, text=sval,
                                         width=width, height=height)
        for ikey, ival in self._informations.items():
            self._d_labels[ikey] = Label(window, text=ival,
                                         width=width, height=height)

        # Positioning of labels
        self._d_labels['title'].grid(row=0, column=0, columnspan=5)
        for sidx, skey in enumerate(self._subsystems):
            self._d_labels[skey].grid(row=sidx+2, column=0)
        for iidx, ikey in enumerate(self._informations):
            self._d_labels[ikey].grid(row=iidx+2+len(self._subsystems),
                                      column=0)

    def buttons(self, window):

        """ Initialize and place all buttons in window. """

        width = 15
        height = 3

        # Dictionary storing all buttons
        self._d_buttons = {}
        for pidx, (pkey, pval) in enumerate(self._plants.items()):
            self._d_buttons[pkey] = \
                Button(window, text=pval,
                       command=lambda pidx=pidx, pval=pval: self._open_sub_window(pidx, pval),
                       width=width, height=height)

        # Positioning of buttons
        for pidx, pkey in enumerate(self._plants):
            self._d_buttons[pkey].grid(row=1, column=pidx+1)

    def indicators(self, window, windowname, show_columns = []):

        """ Initialize and place all indicators in window. Indicators typically
        show if a system is on or off. Show only columns that are in list
        show_columns. If show_columns is empty, show all. """

        width = 15
        height = 2

        # Dictionary storing all indicators
        for pidx, pkey in enumerate(self._plants):
            if show_columns and pidx not in show_columns:
                logging.debug('Skip indicators %s, since index %s is not in show_columns list %s' % (pkey, pidx, show_columns))
                continue
            for skey in self._subsystems:
                gkey = get_global_key([windowname, pkey, skey])
                self._d_indicators[gkey] = \
                    Button(window,
                           text=on_off_text(self._get_data(pkey, skey)),
                           width=width, height=height,
                           bg=on_off_bg(self._get_data(pkey, skey)),
                           command=lambda pkey=pkey, skey=skey: self._action(pkey, skey))

        # Positioning of indicators
        for pidx, pkey in enumerate(self._plants):
            if show_columns and pidx not in show_columns:
                continue
            for sidx, skey in enumerate(self._subsystems):
                gkey = get_global_key([windowname, pkey, skey])
                self._d_indicators[gkey].grid(row=sidx+2, column=pidx+1)

    def _get_data(self, pkey, skey):

        """ Return data from json file for plant key pkey and subsystem key
        skey. Throw error if key combination not found in json file. """

        try:
            return self._data[pkey][skey]
        except KeyError:
            msg = 'The key combination plant \"{}\" and subsystem \"{}\" '\
                  'could not be found in the json file.'.format(pkey, skey)
            logging.error(msg)
            logging.error('Exit.')
            raise

    def _open_sub_window(self, pidx, title):

        """ Function called when pressing the moms button. """

        self.subwin = Tk()
        SubWin(self.subwin, pidx, title)

    def _action(self, pkey, skey):

        """ Action taken depending on pkey and skey. An action is an event that
        happens in real life, e.g. turn on/off light or pump water. """

        try:
            eval(get_global_key([pkey, skey]))()
        except NameError:
            logging.warning('I do not have an action for the name %s()' %
                    get_global_key([pkey, skey]))
        self._toggle(pkey, skey)

    def _toggle(self, pkey, skey):

        """ Toggle on/off indicator with plant key pkey and subsystem key skey.
        """

        logging.info('Toggle %s %s, which currently is %s' % (pkey, skey,
            self._get_data(pkey, skey)))

        # Toggle data
        if self._get_data(pkey, skey) == 1:
            self._data[pkey][skey] = 0
        elif self._get_data(pkey, skey) == 0:
            self._data[pkey][skey] = 1

        # Change color and text of button in master window
        self._d_indicators[get_global_key(['master', pkey, skey])]\
            .configure(bg=on_off_bg(self._get_data(pkey, skey)),
                       text=on_off_text(self._get_data(pkey, skey)))
        # Change color and text of button in slave window (if it exists)
        try:
            self._d_indicators[get_global_key(['slave', pkey, skey])]\
                .configure(bg=on_off_bg(self._get_data(pkey, skey)),
                           text=on_off_text(self._get_data(pkey, skey)))
        except KeyError:
            pass

        # Write changes to file
        self._jsonobject.write(self._data)

        return


class SubWin(MasterWin):

    """ Sub window class for project Alperose. """

    def __init__(self, slave, pidx, title):

        logging.info('Create sub window with index %s and title %s'
                      % (pidx, title))

        self.pidx = pidx
        self.slave = slave
        slave.title(title)

        # Set up all labels, buttons and indicators in slave window
        logging.info('Set up labels in window slave')
        self.labels(self.slave, title)
        #logging.info('Set up buttons in window slave')
        #self.buttons(self.slave)
        logging.info('Set up indicators in window slave')
        self.indicators(self.slave, 'slave', [pidx])
