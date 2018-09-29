#!/usr/bin/env python3

""" Master window module for project Alperose. """

from tkinter import Label, Button
from pprint import pprint
from logger import logging
from DataAccess import DataAccess


class MasterWin:

    """ Master window for project Alperose. """

    def __init__(self, master):
        self.master = master
        master.title('Mario Control Center')

        self._data = self.read_data()

        self.labels()
        self.buttons()
        self.indicators()

    def read_data(self):

        """ Method to read data from json file. """

        return DataAccess('data.json').read()

    def labels(self):

        """ Initialize and place all labels in master window. """

        width = 25
        height = 2

        # Dictionary storing all labels
        self._d_labels = {}
        self._d_labels['title'] = Label(self.master,
                                        text='Super Mario Control Center',
                                        height=height)
        self._d_labels['system'] = Label(self.master, text='System',
                                         width=width, height=height)
        self._d_labels['maintenance'] = Label(self.master, text='Wartung',
                                              width=width, height=height)
        self._d_labels['lamp'] = Label(self.master, text='Lampe', width=width,
                                       height=height)
        self._d_labels['fan'] = Label(self.master, text='Luefter', width=width,
                                      height=height)
        self._d_labels['pump'] = Label(self.master, text='Pumpe', width=width,
                                       height=height)
        self._d_labels['runtime'] = Label(self.master, text='System Laufzeit',
                                          width=width, height=height)
        self._d_labels['water_exchange'] = Label(self.master,
                                                 text='Letzter Wasserwechsel',
                                                 width=width, height=height)
        self._d_labels['temp_air'] = Label(self.master, text='Lufttemperatur',
                                           width=width, height=height)
        self._d_labels['temp_water'] = Label(self.master,
                                             text='Wassertemperatur',
                                             width=width, height=height)

        # Positioning of labels
        self._d_labels['title'].grid(row=0, column=1, columnspan=4)
        self._d_labels['system'].grid(row=2, column=0)
        self._d_labels['maintenance'].grid(row=3, column=0)
        self._d_labels['lamp'].grid(row=4, column=0)
        self._d_labels['fan'].grid(row=5, column=0)
        self._d_labels['pump'].grid(row=6, column=0)
        self._d_labels['runtime'].grid(row=7, column=0)
        self._d_labels['water_exchange'].grid(row=8, column=0)
        self._d_labels['temp_air'].grid(row=9, column=0)
        self._d_labels['temp_water'].grid(row=10, column=0)

    def buttons(self):

        """ Initialize and place all buttons in master window. """

        width = 15
        height = 3

        # Dictionary storing all buttons
        self._d_buttons = {}
        self._d_buttons['moms'] = Button(self.master, text='Mamis',
                                         command=self.moms, width=width,
                                         height=height)
        self._d_buttons['shoots'] = Button(self.master, text='Steckis',
                                           command=self.shoots, width=width,
                                           height=height)
        self._d_buttons['veg'] = Button(self.master, text='Vegis',
                                        command=self.veg, width=width,
                                        height=height)
        self._d_buttons['buds'] = Button(self.master, text='Buds',
                                         command=self.buds, width=width,
                                         height=height)

        # Positioning of buttons
        self._d_buttons['moms'].grid(row=1, column=1)
        self._d_buttons['shoots'].grid(row=1, column=2)
        self._d_buttons['veg'].grid(row=1, column=3)
        self._d_buttons['buds'].grid(row=1, column=4)

    def indicators(self):

        """ Initialize and place all indicators in master window. Indicators
        typically show if a system is on or off. """

        width = 15
        height = 2

        # Set up shortcuts to dictionaries from json data
        moms = self._data['moms']
        shoots = self._data['shoots']
        veg = self._data['veg']
        buds = self._data['buds']

        # Dictionary storing all indicators
        self._d_indicators = {}
        self._d_indicators['mom_system'] = \
            Label(self.master, text=onOffText(moms['system']), width=width, height=height,
                  bg=onOffBg(moms['system']))
        self._d_indicators['mom_maintenance'] = \
            Label(self.master, text=onOffText(moms['maintenance']), width=width, height=height,
                  bg=onOffBg(moms['maintenance']))

        # Positioning of indicators
        self._d_indicators['mom_system'].grid(row=2, column=1)
        self._d_indicators['mom_maintenance'].grid(row=3, column=1)

        # Colors of indicators
        #self._d_indicators['mom_system'].

        #labSystem=Label(self.Hauptfenster,text="System",height=2)
        #self.labSystemZustandMamis=Label(self.Hauptfenster,text=self.systemZustand(0,1),height=2,width=10)
        #self.labSystemZustandSteckis=Label(self.Hauptfenster,text=self.systemZustand(1,1),height=2,width=10)
        #self.labSystemZustandVegis=Label(self.Hauptfenster,text=self.systemZustand(2,1),height=2,width=10)
        #self.labSystemZustandBuds=Label(self.Hauptfenster,text=self.systemZustand(3,1),height=2,width=10)


    def moms(self):

        """ Method called when pressing the moms button. """

        print('Inside function moms()')

    def shoots(self):

        """ Method called when pressing the shoots button. """

        print('Inside function shoots()')

    def veg(self):

        """ Method called when pressing the veg button. """

        print('Inside function veg()')

    def buds(self):

        """ Method called when pressing the buds button. """

        print('Inside function buds()')

def onOffText(n):
    if n == 0:
        return 'OFF'
    else:
        return 'ON'

def onOffBg(n):
    if n == 0:
        return '#D00000'
    else:
        return '#248232'
