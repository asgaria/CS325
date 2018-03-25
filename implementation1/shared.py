from bruteforce import bruteforce

def sortx(p1, p2):
	dx = p1[0] - p2[0]
	if dx != 0:
		return int(dx)
	return int(p1[1] - p2[1])

def sorty(p1, p2):
	dy = p1[1] - p2[1]
	if dy != 0:
		return int(dy)
	return int(p1[0] - p2[0])

def between(lst):
	if len(lst) <= 3:
		return bruteforce(lst)
	
	lhalf = lst[0:len(lst)/2]
	rhalf = lst[len(lst)/2:len(lst)]
	
	d = between(lhalf)
	d_new = between(rhalf)
	
	if d_new[0] < d[0]:
		d = d_new
	elif d_new[0] == d[0]:
		d = (d[0], d[1] + d_new[1])

	min_y = lhalf[-1][1] - d[0]
	max_y = rhalf[ 0][1] + d[0]













	
	d_new = bruteforce( [p for p in lhalf if p[1] > min_y]
	                  + [p for p in rhalf if p[1] < max_y])

	if d_new[0] < d[0]:
		d = d_new
	elif d_new[0] == d[0]:
		d = (d[0], d[1] + [p for p in d_new[1] if p not in d[1]])
		
	return d
