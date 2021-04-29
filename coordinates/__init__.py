import os
import time

"""
h8  ---> 7,7
7,7 ---> h8
"""

def pktool(move,q):
    """
    :param q: 0 = Normal --> Piskvork
    :return:  1 = Piskvork --> Normal
    """
    if q == 0:
        x = move[0]
        y = move[1:]
        return str(ord(x)-97)+','+str(15-int(y))
    if q == 1:
        x = int(move.split(',')[0])
        y = int(move.split(',')[1])
        return str(chr(x+97)) + str(int(15-y))
