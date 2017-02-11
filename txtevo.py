#python3.5

''' taken from `http://usingpython.com/dl/evolutionText.py` '''

import random
import string
import time

posChars = string.ascii_lowercase + string.digits + string.ascii_uppercase + " .,!?;:@#$%^&*()-_=+\\|]}[{'\"/`~"
tar = input("Enter your target text: ")

attempt = "".join(random.choice(posChars) for i in range(len(tar)))
attNext = ""

comp = False
gen = 0

while comp is not True:
	print(attempt)
	attNext = ""
	comp = True
	for i in range(len(tar)):
		if attempt[i] != tar[i]:
			comp = False
			attNext += random.choice(posChars)
		else:
			attNext += tar[i]
	gen += 1
	attempt = attNext
	time.sleep(0.1)

print("Target matched! That took %d generation(s)!" % gen)