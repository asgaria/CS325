from bruteforce import bruteforce
from shared import between

def enhanced(lst, ysorted):
	if (len(lst) <= 3):
		return bruteforce(lst)
	else:
		lhalf = lst[0:len(lst)/2]
		rhalf = lst[len(lst)/2:len(lst)]
		lysorted = [p for p in ysorted if p in lhalf]
		rysorted = [p for p in ysorted if p in rhalf]
		
		d = enhanced(lhalf, lysorted)
		d_new = enhanced(rhalf, rysorted)

		if d_new[0] < d[0]:
			d = d_new
		elif d_new[0] == d[0]:
			d = (d[0], d[1] + d_new[1])
		
		d_new = between( [p for p in lysorted if p[0] > lhalf[-1][0]-d[0]]
		               + [p for p in rysorted if p[0] < rhalf[ 0][0]+d[0]])
		
		
		if d_new[0] < d[0]:
			d = d_new
		elif d_new[0] == d[0]:
			d = (d[0], d[1] + [p for p in d_new[1] if p not in d[1]])
		
		return d
