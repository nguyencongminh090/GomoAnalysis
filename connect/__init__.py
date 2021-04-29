import subprocess


# noinspection PyGlobalUndefined
def connect(engines):
    global engine
    engine = subprocess.Popen(engines, universal_newlines=True,
                              stdin=subprocess.PIPE, stdout=subprocess.PIPE, bufsize=1)


def put(command):
    engine.stdin.write(command + '\n')


def get():
    while True:
        try:
            
            if ',' in text:
                return text
            elif 'MESSAGE' in text:
                print('Engine output:', text)
        except:
            pass


def timeinit(b):
    b = str(int(b) * 1000)
    put('INFO max_memory 0')
    put('INFO timeout_match ' + b)
    put('INFO timeout_turn ' + b)
    put('INFO game_type 0')
    put('INFO rule 1')
    put('INFO time_left ' + b)
    put('START 15')


def ms():
    while True:
        try:
            text = engine.stdout.readline().strip()
            if 'MESSAGE' in text and 'depth' in text:
                sp = text.split(' ')
                depth = sp[sp.index('depth')+1]
                ev = sp[sp.index('ev')+1]
                engine.stdout.readline().strip()
                return [depth, ev]
            if ',' in text:
                return ['1-%NaN%', '0']
        except:
            pass
    
    

    
def kill():
    engine.kill()
