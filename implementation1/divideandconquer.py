from bruteforce import bruteforce
from shared import *

def naive(lst):
	if len(lst) <= 3:
		return bruteforce(lst)

	lhalf = lst[0:len(lst)/2]
	rhalf = lst[len(lst)/2:len(lst)]

	






	
	

	
	d = naive(lhalf)
	d_new = naive(rhalf)
		
	if d_new[0] < d[0]:
		d = d_new
	elif d_new[0] == d[0]:
		d = (d[0], d[1] + d_new[1])

	min_x = lhalf[-1][0] - d[0]
	max_x = rhalf[ 0][0] + d[0]
		
	lst = []
	for i in reversed(xrange(len(lhalf))):
		if lhalf[i][0] > min_x:
			lst.append(lhalf[i])
		else:
			break
		
	for i in xrange(len(rhalf)):
		if rhalf[i][0] < max_x:
			lst.append(rhalf[i])
		else:
			break

	d_new = between(sorted(lst, sorty))

	
	if d_new[0] < d[0]:
		d = d_new
	elif d_new[0] == d[0]:
		d = (d[0], d[1] + [p for p in d_new[1] if p not in d[1]])
	
	return d
