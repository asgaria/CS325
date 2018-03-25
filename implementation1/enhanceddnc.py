from bruteforce import bruteforce
from shared import between

def enhanced(lst, ysorted):
	if len(lst) <= 3:
		return bruteforce(lst)
	
	lhalf = lst[0:len(lst)/2]
	rhalf = lst[len(lst)/2:len(lst)]

	lmax_x = lhalf[-1][0]
	rmin_x = rhalf[ 0][0]
	
	lysorted = []
	rysorted = []
	for p in ysorted:
		if p[0] <= lmax_x:
			lysorted.append(p)
		else:
			rysorted.append(p)
	
	d = enhanced(lhalf, lysorted)
	d_new = enhanced(rhalf, rysorted)
	
	if d_new[0] < d[0]:
		d = d_new
	elif d_new[0] == d[0]:
		d = (d[0], d[1] + d_new[1])
		
	min_x = lmax_x - d[0]
	max_x = rmin_x + d[0]














	d_new = between( [p for p in lysorted if p[0] > min_x]
	               + [p for p in rysorted if p[0] < max_x])
	
	if d_new[0] < d[0]:
		d = d_new
	elif d_new[0] == d[0]:
		d = (d[0], d[1] + [p for p in d_new[1] if p not in d[1]])
	
	return d
