#python3.5

''' print machine; for looking up machine's by their UDC (User Defined Codename) '''

import os
import sys

udc = sys.argv[1].replace("\\", "/") + '/src/udc/local.udc' # the udc doc

usage = """Print Machine
pmac [code]
========================
This program takes one argument, the machine's UDC.
"""

if(len(sys.argv) == 3):
	pass
else:
	print(usage)
	sys.exit(1)

def g(path):
	with open(udc, 'r') as f:
		for line in f.read().split("\n"):
			if not line.startswith("##"):
				yield line.split("::")
			else:
				pass


if __name__ == "__main__":
	if(sys.argv[2] == "-h"):
		print(usage)
		sys.exit(0)
	else:
		p = 0 # print-out counter

		# BEGIN!
		for line in g(udc):
			if(sys.argv[2].lower() == line[0]):
				print("\n" + line[1].replace("|", "\n"))
				p += 1
			else:
				pass

		if(p == 0):
			print("No info for that UDC found")