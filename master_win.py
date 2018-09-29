#!/usr/bin/env python3

""" Master window module for project Alperose """

from tkinter import Label, Button


class MasterWin:

    """ Master window for project Alperose"""

    def __init__(self, master):
        self.master = master
        master.title('Mario Control Center')

        self.labels()
        self.buttons()

    def labels(self):

        """ Place all labels in master window. """

        width = 25
        height = 2

        # Dictionary storing all labels
        self.d_labels = {}
        self.d_labels['title'] = Label(self.master,
                                       text='Super Mario Control Center',
                                       height=height)
        self.d_labels['system'] = Label(self.master, text='System',
                                        width=width, height=height)
        self.d_labels['maintenance'] = Label(self.master, text='Wartung',
                                             width=width, height=height)
        self.d_labels['lamp'] = Label(self.master, text='Lampe', width=width,
                                      height=height)
        self.d_labels['fan'] = Label(self.master, text='Luefter', width=width,
                                     height=height)
        self.d_labels['pump'] = Label(self.master, text='Pumpe', width=width,
                                      height=height)
        self.d_labels['runtime'] = Label(self.master, text='System Laufzeit',
                                         width=width, height=height)
        self.d_labels['water_exchange'] = Label(self.master,
                                                text='Letzter Wasserwechsel',
                                                width=width, height=height)
        self.d_labels['temp_air'] = Label(self.master, text='Lufttemperatur',
                                          width=width, height=height)
        self.d_labels['temp_water'] = Label(self.master,
                                            text='Wassertemperatur',
                                            width=width, height=height)

        # Positioning of labels
        self.d_labels['title'].grid(row=0, column=1, columnspan=4)
        self.d_labels['system'].grid(row=2, column=0)
        self.d_labels['maintenance'].grid(row=3, column=0)
        self.d_labels['lamp'].grid(row=4, column=0)
        self.d_labels['fan'].grid(row=5, column=0)
        self.d_labels['pump'].grid(row=6, column=0)
        self.d_labels['runtime'].grid(row=7, column=0)
        self.d_labels['water_exchange'].grid(row=8, column=0)
        self.d_labels['temp_air'].grid(row=9, column=0)
        self.d_labels['temp_water'].grid(row=10, column=0)

    def buttons(self):

        """ Place all buttons in master window. """

        width = 15
        height = 3

        # Dictionary storing all buttons
        self.d_buttons = {}
        self.d_buttons['moms'] = Button(self.master, text='Mamis',
                                        command=self.moms, width=width,
                                        height=height)
        self.d_buttons['shoots'] = Button(self.master, text='Steckis',
                                          command=self.shoots, width=width,
                                          height=height)
        self.d_buttons['vegis'] = Button(self.master, text='Vegis',
                                         command=self.vegis, width=width,
                                         height=height)
        self.d_buttons['buds'] = Button(self.master, text='Buds',
                                        command=self.buds, width=width,
                                        height=height)

        # Positioning of buttons
        self.d_buttons['moms'].grid(row=1, column=1)
        self.d_buttons['shoots'].grid(row=1, column=2)
        self.d_buttons['vegis'].grid(row=1, column=3)
        self.d_buttons['buds'].grid(row=1, column=4)

    def moms(self):

        """ Method called when pressing the moms button. """

        print('Inside function moms()')

    def shoots(self):

        """ Method called when pressing the shoots button. """

        print('Inside function shoots()')

    def vegis(self):

        """ Method called when pressing the vegis button. """

        print('Inside function vegis()')

    def buds(self):

        """ Method called when pressing the buds button. """

        print('Inside function buds()')
