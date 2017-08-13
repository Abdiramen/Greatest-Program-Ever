#!/usr/bin/env python3
from time import sleep
import os
os.system('setterm -cursor off')
spin = "-\|/"
while True:
    for i in spin:
        sleep(.1)
        print('[{}]'.format(i), end='\r')
print()
os.system('setterm -cursor on')
