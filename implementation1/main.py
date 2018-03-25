from sys import argv
from shared import *
import bruteforce
import divideandconquer
import enhanceddnc

def print_to_file(result, name):
	output_file = open("output_" + name + ".txt", "w")
	output_file.write(str(result[0]) + "\n")
	for pair in sorted(result[1]):
		output_file.write(str(pair[0][0]) + " " + str(pair[0][1]) + " " + str(pair[1][0]) + " " + str(pair[1][1]) + "\n")
	output_file.close()

if __name__ == "__main__":
	input_file = open(argv[2], "r")
	points = []
	
	for line in input_file:
		line = line.split()
		try:
			points.append((int(line[0]), int(line[1])))
		except ValueError:
			points.append((float(line[0]), float(line[1])))
		
	input_file.close()

	xsorted = sorted(points, sortx)

	import time
	t = time.time()
	if argv[1] == "-b":
		print_to_file(bruteforce.bruteforce(xsorted), "bruteforce")
	elif argv[1] == "-d":
		print_to_file(divideandconquer.naive(xsorted), "divideandconquer")
	elif argv[1] == "-e":
		print_to_file(enhanceddnc.enhanced(xsorted, sorted(points, sorty)), "enhanceddnc")
	print time.time() - t
