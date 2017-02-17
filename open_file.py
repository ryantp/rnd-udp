#python3.5

''' python wrapper for opf[.bat]:

formerly:
	@echo off
	start notepad %CD%\%1
... which can't open files in other directories. Time to fix that xD 

works as of 02.16.2017@22:16'''

import os, sys

usage = "opf [Open File] -> opf [filename]"

if __name__ == "__main__":
	# will receive 2 (additional) args: the cwd of the calling shell and the filename
	if len(sys.argv) == 3:
		if sys.argv[2] == '-h':
			print(usage)
		else:
			if "/" in sys.argv[2].replace("\\", "/"):
				# then the filename is an absolute path
				fp = sys.argv[2].replace("\\", "/")
			else:
				if sys.argv[1].replace("\\", "/").endswith("/"):
					fp = sys.argv[1].replace("\\", "/")
				else:
					fp = sys.argv[1].replace("\\", "/") + "/"
				fp += sys.argv[2]
			with os.popen("start notepad %s" % fp) as f:
				pass
	else:
		print(usage)
		sys.exit(1)
else:
	pass
		