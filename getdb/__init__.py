def get(fin):
    try:
        f = open(fin, 'r')
        a = f.read()
        a = a.split('\n\n')    
        return a
    except:
        raise ValueError("Can't open file.")

        
def game(a):
    game = a[1]
    tmp1 = game.split('\n')
    return ' '.join(tmp1)


def chk(string):
    num = []
    for i in string:
        if i.isnumeric():
            num.append(i)
    num = ''.join(num)
    tmp = string.replace(num, '*')
    tmp = tmp.replace('.', '*')
    tmp = tmp.replace('*', '')
    if tmp != '':
        return False
    else:
        return True



def gamefm(v):
    a = game(v)
    tmk = a.split(' ')

    for i in range(len(tmk)):
        if chk(tmk[i]) == True:
            tmk.pop(i)
            tmk.insert(i,'*')
        elif (tmk[i] == 'black') or (tmk[i] == 'white') or (tmk[i] == '--') or (tmk[i] == '0-1') or (tmk[i] == '1-0') or (tmk[i] == '1/2-1/2'):
            tmk.pop(i)
            tmk.insert(i, '*')
    tmk = ' '.join(tmk)
    tmk = tmk.replace('* ', '')
    tmk = tmk.replace('*', '')
    return tmk

def gamedb(v):
    g1 = gamefm(v)
    g1 = g1.split(' ')
    for i in range(len(g1)):
        if g1[i] == '':
            g1.pop(i)
    return g1


def fplay(v):
    v = get(v)
    db = gamedb(v)
    return db


    

############################
# ** Data **
# 0: date
# 1: black
# 2: white
# 3: result
# 4: belo
# 5: welo
############################

############################
# ** Game **
#







    
