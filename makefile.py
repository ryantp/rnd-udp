#python3.5

'''a simple wrapper tool for creating new files of any type.

Note:
	uses `mkf.bat` file to get the arguments for dir and filename'''

__version__ = "1.0.0.1"
__author__ = "Ryan Pelton"
__email__ = "ryantp@gmail.com"
__maintainer__ = "NOT_ACTIVELY_MAINTAINED"
__license__ = "GNU GPL"
__status__ = "Production"

import os, sys


usage = '''\
mkf -> make file
======================
REQUIRES:
-	file name
======================
EXAMPLE:
> mkf example.txt
'''


def file_exists_querey(fn = ''):
	if(os.path.exists(fn)):
		print("ATTN! Filename %s already exists in this directory!" % fn)
		o = input("Overwrite? [y]: ")
		if not o or o.lower().startswith('y'):
			ovw(fn)
		elif o == '/' or o.lower().startswith('n'):
			print("mkf aborting!")
			sys.exit(0)
		else:
			appn(fn)
	else:
		ovw(fn)


def ovw(fn):
	with os.popen("echo //text here>> %s" % fn) as f:
		print("File %s created!" % fn)
		f.close()
	del f


def appn(fn):
	n = "(%d)"
	name = fn.split("/")[-1]
	l = name.split(".")
	for i in range(1, 21):
		# 20 possibilities
		tmpl = l[0] + n % i
		tmpl += '.' + l[1]
		tmpname = name[0:-1]
		tmpname.append(tmpl)
		if not os.path.exists(tmpname):
			break

	with os.popen("echo //text here>> %s" % "/".join(tmpname)) as f:
		print("File %s created!" % "/".join(tmpname))
		f.close()
	del f


def main():
	raw_path = sys.argv[1].replace("\\", "/")
	if raw_path.endswith("/"):
		path = raw_path
	else:
		path = raw_path + "/"

	path += sys.argv[2]
	file_exists_querey(path)


if __name__ == "__main__":
	if(len(sys.argv) == 3):
		main()
	else:
		print(usage)
		sys.exit(1)