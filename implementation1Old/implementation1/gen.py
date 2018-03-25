from sys import argv
import random

n = int(argv[1])

for i in range(0, n):
	print random.randrange(0, n*10), random.randrange(0, n*10)
	
