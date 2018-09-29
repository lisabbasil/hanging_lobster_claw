#!/usr/bin/env python3

from tkinter import Tk
from MasterWin import MasterWin
from logger import logging

if __name__ == '__main__':

    root = Tk()
    my_gui = MasterWin(root)
    root.mainloop()
