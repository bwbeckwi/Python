import sys
from math import log

def convert(s):
	try:
		return int(s)
	except (ValueError, TypeError) as e:
		print ("Conversion error: {}".format(str(e)),file=sys.stderr)
		raise
		#return -1
		

def string_log(s):
	v = convert(s)
	return log(v)
	
	
def sqrt(x):
	guess = x
	i = 0
	while guess * guess != x and i < 20:
		guess = (guess + x / guess) / 2.0
		i += 1
	return guess
	
	
def main():
	print(sqrt(9))
	print(sqrt(2))
	print(string_log(3))
	print(convert(3.14159))

	
if __name__ == '__main__':
	main()