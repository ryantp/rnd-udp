#python3.5

''' a simple help script for the upd/c library; called with `uhelp.bat` '''

import os
import sys

from uhelp import all_scripts as _as
load_c = [ x for x  in os.listdir(sys.argv[1]) if os.path.isfile(sys.argv[1] + x) ] # load all filenames from batch script's dir

for c in load_c:
	p = c.split('.')
	try:
		print("%(p)s\t\t%(d)s" % {
			'p': p[0],
			'd': _as.available_scripts[c]})
	except KeyError:
		pass
