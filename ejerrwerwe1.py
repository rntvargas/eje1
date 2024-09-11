import sys
from time import sleep
import time 

def eclipse():
    lines = [
        ("I'd give the world to ", 0.1),
        ("you.", 0.9),
        ("cause i know the sun,", 0.05),
        ("the moon, the hurt", 0.05),
        ("falls with", 0.06),
        ("you.", 0.9),
        ("i'd give the world to",0.08),
        ("you.", 0.6),
        ("but our eclipse was all",0.07),
        ("that i gave to",0.07),
        ("you.",0.7)
   

    ]

    delays = [0.2, 0.1, 0.1, 0.1,
              0.1, 0.1, 
              1.4, 0.8, 0.4, 0.9, 0.5, 4]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

eclipse()
