#!/usr/bin/env python3

from inspect import currentframe, getframeinfo

def moms_system():
    print(getframeinfo(currentframe()).function)

def moms_maintenance():
    print(getframeinfo(currentframe()).function)
