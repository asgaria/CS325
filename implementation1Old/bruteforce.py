import sys
import numpy as np

def calculate_dist(x,y):
	calc1 = (x[0] - y[0])**2
	calc2 = (x[1] - y[1])**2
	calc3 = (calc1 + calc2) ** 0.5
	return calc3

def print_to_file(cur_min, minimum_points):
	cur_file = open("output_bruteforce.txt", "w")
	cur_file.write(str(cur_min) + "\n")
	
	sort_list = sorted(minimum_points)
	y_sort_list = []
	for a in range(0, len(sort_list)):
		new_sort = sorted(sort_list[a])
		cur_file.write(str(new_sort[0][0]) + " " + str(new_sort[0][1]) + " " + str(new_sort[1][0]) + " " + str(new_sort[1][1]) + "\n") 
		

def bruteforce(): 
	cur_file = open(sys.argv[1], "r")	#opens example.input
	point_list = []				#initial list of points 
	cur_min = 0				#initialize minimum

	minimum_points = []			#list of points that meet the distance requirement

	for line in cur_file:
		line = line.split()
		point = (int(line[0]), int(line[1]))
		point_list.append(point)
	
	if len(point_list) == 1:
		minimum_points.append(point_list[0]);		

	if len(point_list) >= 2:
		new_min = calculate_dist(point_list[0], point_list[1])
		cur_min = new_min 

		for a in range(0, len(point_list) - 1):
			for b in range(a+1, len(point_list)):
				dist = calculate_dist(point_list[a], point_list[b])	
				if dist < cur_min:
					cur_min = dist
					minimum_points = []
					minimum_points.append((point_list[a], point_list[b]))
				elif dist == cur_min:
					minimum_points.append((point_list[a], point_list[b]))

		print_to_file(cur_min, minimum_points)


bruteforce()
