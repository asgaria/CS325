from pulp import *
import numpy as np
import pylab as pl

def minMaxAbsDev():
	pts = [[1, 3], [2, 5], [3, 7], [5, 11], [7, 14], [8, 15], [10, 19]]
	xpt = [1, 2, 3, 5, 7, 8, 10]
	ypt = [3, 5, 7, 11, 14, 15, 19]
	a = LpVariable('a', 0)
	b = LpVariable('b', 0)
	r = LpVariable('r', 0)
	
	prob = LpProblem("maxabsdev", LpMinimize)
	
	for i in range(len(pts)):
		prob += r >= a * pts[i][0] + b - pts[i][1]	
		prob += -r <= a * pts[i][0] + b - pts[i][1]
	prob += r
		#prob += max((a*1 + b - 3), (a*2 + b - 5), (a*3 + b - 7), (a*5 + b - 11), (a*7 + b - 14), (a*8 + b - 15), (a*10 + b - 19))

	status = prob.solve()
	LpStatus[status]
	
	print(value(r))
	print(value(a))
	print(value(b))
#	pl.scatter(xpt, ypt);
#	pl.plot(xpt);	
#	pl.show();
minMaxAbsDev()


