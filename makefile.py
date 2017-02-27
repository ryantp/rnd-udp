#python3.5

'''a simple wrapper tool for creating new files of any type. a Win32 version of unix's `touch` function

Note:
	uses `mkf.bat` file to get the arguments for dir and filename

Limitations:
	for use in current working directory only;
	if a full path in a different location is input, a runtime error will probably occur'''

__version__ = "1.0.0.1"
__author__ = "Ryan Pelton"
__email__ = "ryantp@gmail.com"
__maintainer__ = "NOT_ACTIVELY_MAINTAINED"
__license__ = "GNU GPL"
__status__ = "Production"

import os, sys

if sys.argv[1].replace("\\", "/").endswith("/"):
	batdir = sys.argv[1].replace("\\", "/")
else:
	batdir = sys.argv[1].replace("\\", "/") + "/"

usage = '''\
mkf -> make file
======================
REQUIRES:
-	file name
======================
EXAMPLE:
> mkf example.txt
'''

def pph(fn = ''):
	''' personal place holder; will split fn at the . and return a custom placeholder text '''
	global batdir
	pphdir = "%ssrc/tpl/mkftpl/" % batdir
	ph = {
		'bat': pphdir + 'bat',
		'py': pphdir + 'py', # simple hello world for python
		'c': pphdir + 'c', # hello world for c
		'cpp': pphdir + 'cpp', # hello world for cpp
		'html': pphdir + 'html', # html hello world
		'txt': pphdir + 'txt', # text...
	}
	try:
		return ph[fn.split('.')[-1]]
	except KeyError:
		return 0

def wct(fn = ''):
	# write custom text
	fp = pph(fn)
	if fp:
		with open(fp, 'r') as f:
			txt = f.read()
	else:
		print("err-no 2: missing template")
		txt = "text..."
	with open(fn, 'w') as f:
			f.write(txt)


def file_exists_querey(fn = ''):
	if(os.path.exists(fn)):
		print("ATTN! Filename %s already exists in this directory!" % fn)
		o = input("Overwrite? [y]: ")
		if not o or o.lower().startswith('y'):
			ovw(fn)
		elif o == '/':
			print("mkf aborting!")
			sys.exit(0)
		elif o.lower().startswith('n'):
			appn(fn)
		else:
			print("Unrecognized option, exitting.")
			sys.exit(1)
	else:
		ovw(fn)


def ovw(fn):
	# overwrite / create
	with os.popen("echo //text here>> %s" % fn) as f:
		pass
	del f
	wct(fn)


def appn(fn):
	n = "(%d)"
	name = fn.split("/")[-1]
	l = name.split(".")
	for i in range(1, 1001):
		# 1000 possibilities... just cuz :P
		tmpn = l[0] + n % i + '.' + l[1]
		tmpl = fn.split("/")[0:-1]
		tmpl.append(tmpn)
		if not os.path.exists("/".join(tmpl)):
			break

	with os.popen("echo //text here>> %s" % "/".join(tmpl)) as f:
		pass
	del f


def main():
	raw_path = sys.argv[2].replace("\\", "/")
	if raw_path.endswith("/"):
		path = raw_path
	else:
		path = raw_path + "/"

	path += sys.argv[3]
	file_exists_querey(path)


if __name__ == "__main__":
	if(len(sys.argv) == 4):
		main()
	else:
		print(usage)
		sys.exit(1)