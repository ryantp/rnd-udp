import getpass
import sys

import barcode
from barcode.writer import ImageWriter

MAX_LEN = 15

def make(d):
	name = "C:/Users/%(user)s/Pictures/bcx/%(msg)s" % {"user": getpass.getuser(), "msg": sys.argv[1]}
	bc = barcode.get('code39', d, writer = ImageWriter())
	filename = bc.save(name)

try:
	if sys.argv[1]:
		print("NOTE: barcode.codex: code39(..., add_checksum = False) -- USER-ADDITION") # the source code to pybarcode (barcode) was edited (by me), to not include the checksum
		print("Printing %d/%d" % (len(sys.argv[1]), MAX_LEN))
		if len(sys.argv[1]) <= MAX_LEN:
			try:
				make(sys.argv[1])
			except barcode.errors.IllegalCharacterError as exc:
				print("ERRNO 1: %(exc)s" % {'exc': str(exc)})
		else:
			print("Buffer flush: %d" % (len(sys.argv[1]) - MAX_LEN))
			make(sys.argv[1][:MAX_LEN]) # use all up to buffer point
except IndexError:
	print("ERRNO 0: No string-data provided.")