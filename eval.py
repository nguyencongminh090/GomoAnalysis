import time
def evaluation(num):
    """
    - Max evaluation: 10000
    - Testcase:
    + [19] = 0.19
    + [-30] = -0.3
    + [-227] = -2.27
    + [-225] = -2.25
    + [-M22] = Lose in 22 moves
    + [6500] = +65
    -> Convert to win-rate:
    + [0.19] = (0.19 + 200) / 100 = 50.095%
    """
    try:
        num = int(num)
        if num > 1000:
            f = open('Error.txt', 'a+')
            f.write('*** ' + time.ctime() + ' ***\n')
            msg = 'Raise Error:' + str(num) + ' > ' + '10000'
            f.write(msg+'\n')
            f.write('~' * len(msg) + '\n')
            f.close()
            return 'Error: {} > {}'.format(num, 1000)
        num = ((num / 10 + 100) / 200) * 100        
        return '{}'.format(round(num, 2))
    except:
        if str(num).isascii():
            if '-' in num:
                solve = 'Lose in ' + num.split('-M')[1] + (' moves' if num.split('-M')[1] >= '2' else ' move')
                return 0
            elif 'M' in num:
                solve = 'Win in ' + num.split('M')[1] + (' moves' if num.split('M')[1] >= '2' else ' move')
                return 100
            else:
                f = open('Error.txt', 'a+')
                f.write('*** ' + time.ctime() + ' ***\n')
                msg = 'Raise Error: ' + str(num) + '(Win/Lose)'
                f.write(msg+'\n')
                f.write('~' * len(msg) + '\n')
                f.close()
                raise ValueError(msg + ' (Win/Lose)')
        else:
            f = open('Error.txt', 'a+')
            f.write('*** ' + time.ctime() + ' ***\n')
            msg = 'Raise Error: {} (String)'.format(num)
            f.write(msg+'\n')
            f.write('~' * len(msg) + '\n')
            f.close()
            raise ValueError(msg)


