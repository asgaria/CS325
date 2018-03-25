from math import sqrt

def dist(p1, p2):
	return sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

def bruteforce(lst):
	d = dist(lst[0], lst[1])
	min_points = []
	for i in xrange(len(lst) - 1):
		for j in xrange(i+1, len(lst)):
			d_new = dist(lst[i], lst[j])
			if d_new < d:
				min_points = [(lst[i], lst[j])]
				d = d_new
			elif d_new == d:
				min_points.append((lst[i], lst[j]))
	return (d, min_points)
