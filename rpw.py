#python3.5

''' a script that creates a random string, for random password creation -- stores in a .txt file '''

import getpass
import os
import random
import string
import sys

uc = string.ascii_letters + string.digits + "_*&"
ofile = "C:/Users/%(usr)s/Documents/of/rpw/rpw.txt"

rstr = []

try:
	rng = int(sys.argv[1])
except IndexError:
	print("err-no 1: rpw requires a length integer")
	sys.exit(1)
except ValueError:
	if sys.argv[1] == '-h' or sys.argv[1] == '--help':
		print("Usage: rpw [STRING_LENGTH]")
		print("[-f] -> ouput to ", end = '')
		print(ofile % {'usr': getpass.getuser()})
		sys.exit(0)
	else:
		print("err-no 1: rpw requires a length integer")
		sys.exit(1)

for i in range(rng):
	rstr.append(random.choice(uc))

try:
	if sys.argv[2] == '-f':
		with open(ofile % {'usr': getpass.getuser()}, 'a') as f:
			# gets current user through PATH, so this should work most times
			f.write("%s\n" % "".join(rstr))
except IndexError:
	print("".join(rstr))
	