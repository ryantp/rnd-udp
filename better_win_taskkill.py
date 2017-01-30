#python3.5

'''a better implementation of taskkill'''

from os import popen
import sys

if(sys.platform.lower().startswith('win')):
    pass
else:
    print("This is a Windows function")
    sys.exit(1)

hbanner = '''\
tkill -- Win32 tasklist + taskkill tool, implemented with python
usage: tkill [OPTIONS] <process_name>/<process_id>

adv flags: [-h; -c; -p; -l; -a]

    -h -- help
    -c -- list top CPU consuming processes
    -l -- tasklist
    -p -- pid <process_name>
    -a -- killall <process_name>
===================================================================
INFO:
    <process_name>: name of running process; input either FULL
        PROCESS NAME (with `.exe` at the end, ie. 'notepad.exe') or
        PARTIAL PROCESS NAME (ie. 'notepad')
'''

mbanner = '''\
%(usr)s -- tkill

    [L]ist Processes
    [P]rocess ID
    [K]ill
    [A]ll, kill
    [Q]uit

'''

CMD = {
    'TK': 'taskkill /pid %(pid)d',
    'TL': 'tasklist',
    'TKH': 'taskkill /?',
    'TLH': 'tasklist /?',
    'TKIM': 'taskkill /im %(exe)s',
    'TLV': 'tasklist /v'
}


def h():
    global hbanner
    print(hbanner)


def l():
    # tasklist
    global CMD
    with popen(CMD['TL'], 'r') as f:
        for line in f.read().split('\n'):
            print(line)


def p(name = ''):
    # get pid of named process
    global CMD
    if name.endswith('.exe'):
        pass
    else:
        name += '.exe'
    l = []
    tmp = []
    with popen(CMD['TLV'], 'r') as f:
        for line in f.read().split('\n'):
            tmp.append(line.split(' '))
        f.close()
    del f
    for t in tmp:
        if name in t:
            l.append([x for x in t if x])

    for i, _ in enumerate(l):
        print("%(n)s - %(d)d - %(t)s" % {'n': l[i][0], 'd': int(l[i][1]), 't': l[i][-1]})


def k(im = '', pid = 0):
    global CMD
    if(pid):
        with popen(CMD['TK'] % {'pid': pid}, 'r') as f:
            print(f.read())
            f.close()
        del f
    else:
        with popen(CMD['TKIM'] % {'exe': im}, 'r') as f:
            print(f.read())
            f.close()
        del f


def q(name = ''):
    # run tasklist; return all lines running <name> process
    global CMD
    Q = []
    c = -1 # init c; if invalid option is given, will return to main, instead of crashing
    if name.endswith('.exe'):
        pass
    else:
        name += '.exe'
    l = []
    tmp = []
    with popen(CMD['TLV'], 'r') as f:
        for line in f.read().split('\n'):
            tmp.append(line.split(' '))
        f.close()
    del f
    for t in tmp:
        if name in t:
            l.append([x for x in t if x])

    for i, _ in enumerate(l):
        Q.append(['%(n)s' % {'n': l[i][0]}, '%(d)d' % {'d': int(l[i][1])}, '%(t)s' % {'t': " ".join(l[i][8:])}])

    print("Select a process")
    for j, q in enumerate(Q):
        print("%d >>> %s" % (j, "\t".join(q)))
    try:
        c = int(input("Terminate Process: "))
    except ValueError:
        pass
    if(c > len(Q) - 1 or c < 0):
        print("Invalid choice.")
    else:
       k(pid = int(Q[c][1]))


def clear():
    from os import system
    system("cls")
    del system


def main():
    # interactive taskkill list
    global mbanner
    from getpass import getuser as _usr
    m2 = 'action (l, p, k, a, q): '
    loccmd = ['l', 'p', 'k', 'a', 'c']

    clear()
    print(mbanner % {'usr': _usr()})
    while(1):
        print(m2, end = "")
        a = input()
        if a in loccmd:
            if a.lower() == 'k':
                c = input("Process name [kill]: ")
                q(name = c)
            elif a.lower() == 'a':
                c = input("Process name [killall]: ")
                k(im = c)
            elif a.lower() == 'p':
                c = input("Process name: ")
                p(name = c)
            elif a.lower() == 'l':
                l()
            elif a.lower() == 'c':
                clear()
        elif(a.lower() == 'h'):
            h()
        elif(a.lower() == 'q'):
            sys.exit(0)
        else:
            print("UNK CMD -- %(c)s" % {'c': a})
    

def parse(args = []):
    # takes sys.argv[1:] (everything besides the program name) and executes an appropriate action
    pass


if(len(sys.argv) > 1):
    parse(sys.argv[1:])
else:
    main()

