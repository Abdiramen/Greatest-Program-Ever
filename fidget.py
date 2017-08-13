#!/usr/bin/env python3
from time import sleep
import os
os.system('setterm -cursor off')
spin = "-\|/"
try:
    while True:
        for i in spin:
            sleep(.1)
            print('[{}]'.format(i), end='\r')
except KeyboardInterrupt:
    print('\rThank you')
    os.system('setterm -cursor on')
