#python3.5

''' python implementation of Linux's sha checksum function; uses sha1 hash'''

__version__ = "1.0.0.1"
__author__ = "Ryan Pelton"
__email__ = "ryantp@gmail.com"
__maintainer__ = "NOT_ACTIVELY_MAINTAINED"
__license__ = "GNU GPL"
__status__ = "Production"

import hashlib as h
import sys

usage = '''\
sha -> sha1 checksum function; [file] [?sha_value]
==================================================
Calculates the sha sum of the given file

#==========SHA_VAL=========
# sha values:
#	1 == sha1
#	2 == sha224
#	3 == sha256
#	4 == sha384
#	5 == sha512
#	11 == md5
#==========================
'''


def main(fn = '', sv = 1):
	SHA = {
		1: h.sha1,
		2: h.sha224,
		3: h.sha256,
		4: h.sha384,
		5: h.sha512,
		11: h.md5
	}

	s = SHA[sv]()

	with open(fn, 'r') as f:
		for line in f.read():
			s.update(str(line).encode("utf-8"))

	m = s.hexdigest()
	print(m)


if __name__ == '__main__':
	#print(len(sys.argv))
	if(len(sys.argv) > 1 and len(sys.argv) < 5):
		if(sys.argv[2] == '-h'):
			print(usage)
			sys.exit(0)

		raw_path = sys.argv[1].replace("\\", "/")
		if raw_path.endswith("/"):
			path = raw_path
		else:
			path = raw_path + "/"

		try:
			path += sys.argv[2]
		except IndexError:
			print("No filename supplied")
			sys.exit(1)

		try:
			sv = int(sys.argv[3])
		except ValueError:
			print("Invalid SHA_VAL: %s" % str(sys.argv[3]))
			sys.exit(2)
		except IndexError:
			sv = 1

		main(fn = path, sv = sv)
	else:
		print(usage)
		sys.exit(1)
	
