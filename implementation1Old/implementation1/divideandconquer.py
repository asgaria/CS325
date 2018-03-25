from bruteforce import bruteforce
from shared import *

def naive(lst):
	lst = sorted(lst)
	if (len(lst) <= 3):
		return bruteforce(lst)
	else:
		lhalf = lst[0:len(lst)/2]
		rhalf = lst[len(lst)/2:len(lst)]
		
		d = naive(lhalf)
		d_new = naive(rhalf)
		
		if d_new[0] < d[0]:
			d = d_new
		elif d_new[0] == d[0]:
			d = (d[0], d[1] + d_new[1])

		m = []
		for p in lhalf:
			if p[0] > lhalf[-1][0]-d[0]:
				m.append(p)
		for p in rhalf:
			if p[0] < rhalf[0][0]-d[0]:
				m.append(p)
					
		sorted_m = sorted(m, sorty)		
		d_new = between(sorted_m)

		if d_new[0] < d[0]:
			d = d_new
		elif d_new[0] == d[0]:
			d = (d[0], d[1] + [p for p in d_new[1] if p not in d[1]])

		return d
