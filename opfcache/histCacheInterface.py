#python3.5

''' get && set histcache.txt info '''

HARDPATH = "C:/udp/c/src/opfcache/histcache.txt"

# read histcache
def getHistCache():
	global HARDPATH
	try:
		with open(HARDPATH, 'r') as f:
			i = 0
			for line in f.read().split("\n"):
				print("%d -- %s" % (i, line))
				i += 1
	except FileNotFoundError:
		# create the histcache.txt file
		with open(HARDPATH, 'w') as f:
			pass

# capture cache in a list, pop the 0'th element and add a new item
def updateHistCache(new_entry = ''):
	global HARDPATH
	if new_entry:
		try:
			with open(HARDPATH, 'r') as f:
				entry_list = f.read().split("\n")
			if(len(entry_list) >= 10):
				del entry_list[0]
			else:
				pass
			entry_list.append(new_entry)
			with open(HARDPATH, 'w') as f:
				f.write("\n".join(entry_list))
		except FileNotFoundError:
			with open(HARDPATH, 'w') as f:
				f.write(new_path) # add new_path as the first entry
	else:
		pass
