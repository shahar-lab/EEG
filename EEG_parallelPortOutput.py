#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
parallel ports demo

This is for win32 only.
"""

from __future__ import absolute_import, division, print_function

from builtins import range
from psychopy import visual, core
from psychopy import parallel
import time

parallel.setPortAddress((0x5EFC))  # address for parallel port on many machines

while True:
    parallel.setData(0)
    parallel.setPin(2, 1)  # sets just this pin to be high
    time.sleep(1)
    parallel.setData(0)
    #parallel.setPin(3, 1)
    time.sleep(1)
    parallel.setData(0)
    parallel.setPin(4, 1)
    time.sleep(1)




