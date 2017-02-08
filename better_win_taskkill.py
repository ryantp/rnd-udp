#python3.5

'''a better implementation of taskkill on Windows

-- TO-BE-ADDED --
CPU Usage tasklist'''

__version__ = '1.0.1.2'
__license__ = "GNU GPL"
__author__ = 'ryantp'
__email__ = 'ryantp92@gmail.com'
__maintainer__ = "NOT_ACTIVELY_MAINTAINED"
__status__ = "Development"

import argparse
from os import popen
import sys

if(sys.platform.lower().startswith('win')):
    pass
else:
    print("This is a Windows function")
    sys.exit(1)

# help information for interactive tool
hbanner = '''\
tkill v%(v)s -- Win32 tasklist + taskkill tool, implemented with python
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
''' % {'v': __version__}

# options banner; appears when tool launches -- will not be reprinted if screen is cleared
mbanner = '''\
tkill -- interactive

    [L]ist Processes
    [P]rocess ID
    [K]ill
    [A]ll, kill
    [Q]uit

    [H]elp
    [C]lear screen

'''

CMD = {
    'TK': 'taskkill /pid %(pid)d',
    'TL': 'tasklist',
    'TKH': 'taskkill /?',
    'TLH': 'tasklist /?',
    'TKIM': 'taskkill /im %(exe)s',
    'TLV': 'tasklist /v'
}


def help():
    global hbanner
    print(hbanner)


def check_pname(pname = ''):
    if pname.endswith('.exe'):
        return pname
    elif '.' in pname:
        return pname
    else:
        if(pname):
            return pname + '.exe'
        else:
            sys.exit(3)


def tlist(v = 0):
    # tasklist
    '''VERBOSENESS:
    0 = standard tasklistk output; no -v OR -q
    1 = verbose [-v]; tasklist /v
    -1 = quiet [-q]; only name and pid
    ###
    defaults to 0 / standard output'''
    global CMD
    if(v == 0):
        with popen(CMD['TL'], 'r') as f:
            for line in f.read().split('\n'):
               print(line)
    elif(v == 1):
        with popen(CMD['TLV'], 'r') as f:
           for line in f.read().split('\n'):
               print(line)
    elif(v == -1):
        # run tasklist; return all lines running <name> process
        tmp_values = []
        datalist = []
        items = []
        with popen(CMD['TL'], 'r') as f:
            for line in f.read().split('\n'):
                tmp_values.append(line)
            f.close()
        del f
        for tmp in tmp_values[5:-1]:
            datalist.append([ t for t in tmp.split(' ') if t])
        del tmp_values
        for sublist in datalist:
            name = []
            pid = 0
            for value in sublist:
                try:
                    pid = int(value)
                    break
                except ValueError:
                    name.append(value)
            print("%s\t--\t%d" % (" ".join(name), pid))
    else:
        pass


def pid(pname = ''):
    # get pid of named process
    global CMD
    l = []
    tmp = []
    with popen(CMD['TLV'], 'r') as f:
        for line in f.read().split('\n'):
            tmp.append(line.split(' '))
        f.close()
    del f
    for t in tmp:
        if pname in t:
            l.append([x for x in t if x])

    for i, _ in enumerate(l):
        print("%(n)s - %(d)d - %(t)s" % {'n': l[i][0], 'd': int(l[i][1]), 't': l[i][-1]})


def kill(pid = 0):
    # taskkill /pid <pid> # only called through query
    global CMD
    if(pid):
        with popen(CMD['TK'] % {'pid': pid}, 'r') as f:
            print(f.read())
            f.close()
        del f


def killall(im = ''):
    # taskkill /im <name> # requires exact for <name>
    global CMD
    if(im):
        with popen(CMD['TKIM'] % {'exe': im}, 'r') as f:
            print(f.read())
            f.close()
        del f


def query(pname = ''):
    # run tasklist; return all lines running <name> process
    global CMD
    Q = []
    c = -1 # init c; if invalid option is given, will return to main, instead of crashing
    l = []
    tmp = []
    with popen(CMD['TLV'], 'r') as f:
        for line in f.read().split('\n'):
            tmp.append(line.split(' '))
        f.close()
    del f
    for t in tmp:
        if pname in t:
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
       kill(pid = int(Q[c][1]))


def clear():
    from os import system
    system("cls")
    del system

def main():
    # interactive taskkill list
    global mbanner
    m2 = 'action (l, p, k, a, q): '
    lcmd = ['l', 'p', 'k', 'a', 'c']

    #clear()
    print(mbanner)
    while(1):
        print(m2, end = "")
        a = input()
        if a in lcmd:
            if a.lower() == 'k':
                c = input("Process name [kill]: ")
                query(pname = c)
            elif a.lower() == 'a':
                c = input("Process name [killall]: ")
                killall(im = c)
            elif a.lower() == 'p':
                c = input("Process name: ")
                pid(pname = c)
            elif a.lower() == 'l':
                tlist()
            elif a.lower() == 'c':
                clear()
        elif(a.lower() == 'h'):
            help()
        elif(a.lower() == 'q'):
            sys.exit(0)
        else:
            print("UNK CMD -- %(c)s" % {'c': a})
    

parser = argparse.ArgumentParser(prog = "tkill v%(v)s [better_win_taskkill]" % {'v': __version__},
    description = "%(prog)s -- a python wrapper for Windows tasklist & taskkill",
    epilog = "running tkill without optional args will run the standard kill <pname>")

lOut = parser.add_mutually_exclusive_group()
lOut.add_argument('-v', '--verbose', action = 'store_true', help = 'tasklisk verbose results')
lOut.add_argument('-q', '--quiet', action = 'store_true', help = 'minimal tasklist output')

parser.add_argument('pname', nargs = "?", action = 'store', help = "process to spotlight")
parser.add_argument('-c', '--cpu', action = 'store_true', help = "list processes by their cpu usage, highest-lowest")
parser.add_argument('-l', '--list', action = 'store_true', help = "list all running functions")
parser.add_argument('-p', '--pid', action = 'store_true', help = "list the process ID for all instancs of a given function name")
parser.add_argument('-u', '--uselstr', action = 'store_true', help = "use literal string passed by the user, without altering it")

args = parser.parse_args()

if(args.pname):
    # handle events which revolve around pname
    if(args.uselstr):
        if(args.pid):
            pid(pname = args.pname)
        else:
            query(pname = args.pname)
    else:
        name = check_pname(args.pname)
        if(args.pid):
            pid(pname = name)
        else:
            query(pname = name)
elif(args.list):
    # list running processes
    v = 0 # code-int for verboseness
    if(args.quiet):
        v = -1
    elif(args.verbose):
        v = 1
    else:
        pass
    tlist(v = v)
elif(args.cpu):
    # list processes by cpu usage -- to-be-added
    print("ATTN: this function is not yet active!")
else:
    main()

