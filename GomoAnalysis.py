## Analysis Foward

## TODO: Change --> Backward
from colorama import init, Fore, Style
from coordinates import pktool
from getdb import fplay
from connect import *
import connect
from eval import evaluation
import matplotlib.pyplot as plt
import time
import os


def main():
    init()
    # Solve data input
    inpdb = input('Data input: ')
    data = fplay(inpdb)
    arr = []
    for i in range(len(data)):
        arr.append(pktool(data[i], 0))
    inp = input('Time analysis: ')
    engine = input('Engine: ')
    connect.connect('Engine\\' + engine + '.exe')
    print('Option 1: AlphaGomoku\nOption 2: Other')
    option = input('Option: ')
    
    timeinit(inp)
    time.sleep(0.3)
    print('Sleep 5 sec...')
    print('Total moves:', len(arr) - 2)
    b_ev = []
    w_ev = []
    b_num = []
    w_num = []
    print(arr)
    for i in range(len(arr)):
        if i == len(arr) - 1:
            if i % 2 == 0:
                b_ev.append(100-w_ev[-1])
                w_ev.append(w_ev[-1])
                b_num.append(2*i)
            else:
                w_ev.append(100-b_ev[-1])
                b_ev.append(b_ev[-1])
                b_num.append(2*i - 1)
            break
        if 2 < i < len(arr):
            print(Fore.LIGHTRED_EX + '[{}]:'.format(i), Style.RESET_ALL, arr[i])
            put('BOARD')
            for j in range(i + 1):
                if i % 2 == j % 2:
                    put(arr[j] + ',2')
                    #time.sleep(0.1)
                else:
                    put(arr[j] + ',1')
            put('DONE')
            output = connect.ms()
            if option == '2':
                print('Depth: {} - Evaluation: {} - Default output: {}'.format(output[0], round(100 - float(evaluation(output[1])), 2), output[1]))
                if i % 2 == 0:
                    b_ev.append(round(100 - float(evaluation(output[1])), 2))
                    b_num.append(i)
                else:
                    w_ev.append(round(float(evaluation(output[1])), 2))
                    w_num.append(i)
            else:
                print('Depth: {} - Evaluation: {}'.format(output[0], round(100 - float(output[1]), 2)))
                if i % 2 == 0:
                    b_ev.append(100 - float(output[1]))
                    w_ev.append(float(output[1]))
                    b_num.append(2*i)
                else:
                    w_ev.append(100 - float(output[1]))
                    b_ev.append(float(output[1]))
                    b_num.append(2*i - 1)
            put('RESTART')

    connect.kill()
    print('[+] Eval of black:', b_ev)
    print('[+] Eval of white:', w_ev)
    plt.title('Evaluate Graph ' + inp + ' sec')
    plt.plot(b_num, b_ev, 'b.-', label='Black evaluate')
    #plt.plot(w_num, w_ev, 'r.-', label='White evaluate')
    plt.legend(loc='best')
    plt.show()
if __name__ == '__main__':
    main()
    os.system('pause>nul')
