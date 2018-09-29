#!/usr/bin/env python3

import logging
from tkinter import Tk
from master_win import MasterWin

if __name__ == '__main__':
    # Set up logger
    # DEBUG (10), INFO (20), WARNING (30), ERROR (40), CRITICAL (50)
    logging.basicConfig(format='%(levelname)-8s - %(message)s',
                        level=logging.DEBUG)

    root = Tk()
    my_gui = MasterWin(root)
    root.mainloop()
