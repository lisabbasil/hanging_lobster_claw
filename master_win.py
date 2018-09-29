#!/usr/bin/env python3

""" Master window module for project Alperose """

from tkinter import Label, Button


class MasterWin:

    """ Master window for project Alperose"""

    # pylint: disable=too-many-instance-attributes

    def __init__(self, master):
        self.master = master
        master.title('Mario Control Center')

        # GUI control variables
        self.l_width = 25
        self.l_height = 2
        self.b_width = 15
        self.b_height = 3

        # Title
        self.l_title = Label(master, text='Super Mario Control Center',
                             height=self.l_height)
        self.l_title.grid(row=0, column=1, columnspan=4)

        # Labels
        self.l_system = Label(master, text='System', width=self.l_width,
                              height=self.l_height)
        self.l_system.grid(row=2, column=0)
        self.l_maintenance = Label(master, text='Wartung', width=self.l_width,
                                   height=self.l_height)
        self.l_maintenance.grid(row=3, column=0)
        self.l_lamp = Label(master, text='Lampe', width=self.l_width,
                            height=self.l_height)
        self.l_lamp.grid(row=4, column=0)
        self.l_fan = Label(master, text='Luefter', width=self.l_width,
                           height=self.l_height)
        self.l_fan.grid(row=5, column=0)
        self.l_pump = Label(master, text='Pumpe', width=self.l_width,
                            height=self.l_height)
        self.l_pump.grid(row=6, column=0)
        self.l_runtime = Label(master, text='System Laufzeit',
                               width=self.l_width, height=self.l_height)
        self.l_runtime.grid(row=7, column=0)
        self.l_water_change = Label(master, text='Letzter Wasserwechsel',
                                    width=self.l_width, height=self.l_height)
        self.l_water_change.grid(row=8, column=0)
        self.l_temp_air = Label(master, text='Lufttemperatur',
                                width=self.l_width, height=self.l_height)
        self.l_temp_air.grid(row=9, column=0)
        self.l_temp_water = Label(master, text='Wassertemperatur',
                                  width=self.l_width, height=self.l_height)
        self.l_temp_water.grid(row=10, column=0)

        # Buttons
        self.b_moms = Button(master, text='Mamis', command=self.moms,
                             width=self.b_width, height=self.b_height)
        self.b_moms.grid(row=1, column=1)
        self.b_shoots = Button(master, text='Steckis', command=self.shoots,
                               width=self.b_width, height=self.b_height)
        self.b_shoots.grid(row=1, column=2)
        self.b_vegis = Button(master, text='Vegis', command=self.vegis,
                              width=self.b_width, height=self.b_height)
        self.b_vegis.grid(row=1, column=3)
        self.b_buds = Button(master, text='Buds', command=self.buds,
                             width=self.b_width, height=self.b_height)
        self.b_buds.grid(row=1, column=4)

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
