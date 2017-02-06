import argparse

parser = argparse.ArgumentParser(prog = "test.py")
parser.add_argument('inp', nargs = '?', action = 'store')
parser.add_argument('out', nargs = '?', action = 'store')

args = parser.parse_args()

if(args.inp):
	print('y')
else:
	print('n')