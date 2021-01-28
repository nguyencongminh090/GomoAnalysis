from colorama import init, Fore, Style
from coordinates import pktool
from getdb import fplay
import connect
import time
import os


def main():
    init()
    # Solve data input
    inpdb = input('Data input: ')
    data = fplay(inpdb + '.txt')
    arr = []
    wp = 0
    bp = 0
    for i in range(len(data)):
        arr.append(pktool(data[i], 0))
    inp = input('Time analysis: ')
    connect.connect('Engine\\engine.exe')
    connect.timeinit(inp)
    time.sleep(0.3)
    # Analysis game
    for i in range(len(arr)):
        print(Fore.LIGHTRED_EX + '[{}]:'.format(i), Style.RESET_ALL, arr[i])
        if i > 2 and i != len(arr) - 1:
            if i % 2 == 0:
                connect.put('BOARD')
                time.sleep(0.3)
                for j in range(i):
                    if j % 2 == 0:
                        connect.put(arr[j] + ',1')
                    else:
                        connect.put(arr[j] + ',2')
                    time.sleep(0.3)
                connect.put('DONE')
                output = connect.get()
                print('-->', output)
                if output == arr[i]:
                    bp += 1
                connect.put('RESTART')
            else:
                connect.put('BOARD')
                time.sleep(0.3)
                for j in range(i + 1):
                    if j % 2 == 0:
                        connect.put(arr[j] + ',2')
                    else:
                        connect.put(arr[j] + ',1')
                    time.sleep(0.3)
                connect.put('DONE')
                output = connect.get()
                print('-->', output)
                if output == arr[i]:
                    wp += 1
                connect.put('RESTART')
    connect.kill()
    print('--> Accuracy:')
    print('[+] Black: %.2f' % ((bp / (len(arr) - 4)) * 100), '%')
    print('[+] White: %.2f' % ((wp / (len(arr) - 3)) * 100), '%')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('[+] Black good moves:', bp)
    print('[+] White good moves:', wp)


if __name__ == '__main__':
    main()
    os.system('pause>nul')
