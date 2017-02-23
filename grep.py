#!C:\Anaconda3

import argparse, os, re, sys

# python version of grep -- for use outside of Linux / OSX 

# how to == py pygrep.py <file> <string to grep>


"""
ABOUT:

A Python grep tool for use in Windows env (since win doesn't support grep (! not mentioning the win-10 Linux support... :P ) natively).

Currently this script will print whole lines (in-context) of the search string.
"""


VER_NO = "v1.3" 

VERSION_NOTES = r'''JUNE 10 @1956:

+to v1.3:
	-	added compare_file() to program
'''

h_info = \
r'''- Make sure the file being grepped is saved in ANSI
		format  this program has trouble with UNICODE
- Full file paths, unless the file is within the same
		directory 
'''

e_snip = \
r'''
## basic grep:

>>>		pygrep.py <file_name.file_ext> <string_to_search_for>

e.g.	pygrep.py example.txt "hello"

## output to file:

>>>		pygrep.py <file> <string> -f <output_file_path>

		
e.g.	pygrep.py example.txt "hello" -f "example_res.txt"


** other notes


#
#	be aware that this program does not (currently)
#	parse text (in non .txt documents).
#
#	this means, if reading from a(n) .rtf file (Rich Text File)
#	any text used to render the font within the application
#	to edit the file will remain, such as [\f1] or [\b], etc.
#
#	the same would apply to .html files, where the HTML tags
#	will be present in the returned text.
#
#	<title>Website Title</title> <- for example 
#
'''


# CLI PARSER -- set-up 
par = argparse.ArgumentParser(prog = 'pygrep', prefix_chars = '-',
	description = 'ASCII grep tool (CLI) only -- type [-h/--help] for assistance.') 
par.add_argument('file', nargs = '?', type = argparse.FileType('r'),
	default = None, help = 'file to grep') 
par.add_argument('string', nargs = '?', action = 'store',
	help = 'string to search for within file') 
par.add_argument('-f', '--fout', action = 'store', help = 'output info to file FOUT') 
par.add_argument('-i', '--info', action = 'store_true', help = 'other help information') 
par.add_argument('-e', '--example', action = 'store_true', help = 'display example(s) for using pygrep') 
par.add_argument('-v', '--version', action = 'version', version = '%(prog)s {}'.format(VER_NO),
	help = 'displays tool version')
par.add_argument('-r', '--retast', action = 'store', help = 'Replace Target String')
par.add_argument('-c', '--compare', action = 'store', help = 'display differences between two files')
par.add_argument('-a', '--author', action = 'store_true', help = 'display program author') 





def grep_file(search_string):
	print('\n/**\n')
	for line in args.file:
		if re.search(search_string, line):
			try:
				print(line)
			except UnicodeEncodeError:
				print(line.encode("utf-8"))
		else:
			pass 
	print('\n**/\n')

def grep_output_to_file(search_string):
	output_file_name = args.fout 
	
	# original standard output 
	temp = sys.stdout 

	# output to file 
	sys.stdout = open(output_file_name, "w+") 

	

	for line in args.file:
		if re.search(search_string, line):
			print(line + '\n') 
		else:
			pass 
	
	sys.stdout.close() 
	sys.stdout = temp 
	print('Finished') 


def retast(target_string, file_name, replacement_string):
	#RETAST (RE-place TA-rget ST-ring)
	tmpvar = file_name.split('.')
	tmp_file = tmpvar[0] + '_t_'
	with open(tmp_file, 'w') as _:
		pass

	print('\n/**\n')
	with open(file_name, 'r') as f:
		for line in f:
			if re.search(target_string, line):
				print("%(line)s -> " % {'line': line.replace('\n', '').replace('\t', '')}, end = '')
				nline = line.replace(target_string, replacement_string)
				with open(tmp_file, 'a') as _:
					_.write(nline)
					print(nline)
			else:
				with open(tmp_file, 'a') as _:
					_.write(line)
	print('\n**/\n')
	os.system('del %(fn)s' % {'fn': file_name})
	os.system('ren %(tmp)s %(org)s' % {'tmp': tmp_file, 'org': file_name})


def compare_files(compare_type):
	'''prints lines that aren't identical to eachother'''
	display_field = '''

	File 1:
		%s

	%%%%%%%%

	File 2:
		%s
	============'''# % (line1, line2)
	print('\n------------------------\n')
	with open(args.string, 'r') as cf:
		try:
			cfo = cf.read()
			cf.close()
		except Exception as e:
			print('Could not read file\n\n' + e)
		if (compare_type == '+'):
			for line1 in args.file:
				for line2 in cfo:
					if (line1 == line2):
						print(display_field % (line1, line2))
					else:
						pass
		elif (compare_type == '-'):
			for line1 in args.file:
				for line2 in cfo:
					if (line1 != line2):
						if (re.search(line1, line2)):
							pass
						elif (line1 == '' or line1 == ' ' or line2 == '' or line2 == ' '):
							pass
						else:
							print(display_field % (line1, line2))
					else:
						pass
		else:
			print('Unknown comparison type, program exiting')
			exit()
	print('\n------------------------\n')

args = par.parse_args() 

if (args.fout):
	try:
		grep_output_to_file(args.string) 
	except Exception as e:
		print(e)
elif (args.retast):
	retast(target_string = args.string, file_name = args.file, replacement_string = args.retast)
else:
	if not args.author and not args.info and not args.example and not args.compare:

		# if [-a/--author] or [-i/--info] is included, then grep_file() won't run 
		if not args.string:
			print("No search string was provided")
		else:
			grep_file(args.string) 
	elif (args.author):
		print('pygrep -- arkat-one <arcius0@gmail.com>') 
	elif (args.info):
		print(h_info) 
	elif (args.example):
		print(e_snip) 
	elif (args.compare):
		compare_files(args.compare)
	else:
		print('No options or file path were provied  type `pygrep.py -h` for help')
