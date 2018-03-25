from pulp import *
import math
import csv
import pylab as pl
import numpy as np
d = []
temps = [] 

with open('Corvallis.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
            avg = row[7].strip()
            if(not avg.isalpha()):
            	temps.append(float(avg))
            day = row[8].strip()
            if(not day.isalpha()):
            	d.append(float(day))


def warm_up():

	li = 0
	sp = 0
	sc = 0

	prob = LpProblem("seasonal_weather", LpMinimize)

	r = LpVariable("r",0)
	prob += r
	x0 = LpVariable("x0")
	x1 = LpVariable("x1")
	x2 = LpVariable("x2")
	x3 = LpVariable("x3")
	x4 = LpVariable("x4")
	x5 = LpVariable("x5")
	curvey = []
	for i in range(len(d)):
		li = x0 + x1 * d[i];	
		sp = (x2 * math.cos((2 * math.pi * d[i]) / 365.25 )) + (x3 * math.sin((2 * math.pi * d[i]) / 365.25))
		sc = (x4 *  math.cos((2 * math.pi * d[i]) / (365.25 * 10.7))) + (x5 * math.sin((2 * math.pi * d[i]) / (365.25 * 10.7)))	
		prob += r >= (li + sp + sc - temps[i])
		prob += r >= -(li + sp + sc - temps[i])
	
	status = prob.solve()
	
	pl.scatter(d,temps);
	x = np.linspace(0,1, len(d))
	y = []
	for j in range(len(d)):
		y.append(value(x0)+value(x1) *d[j]);	
		li = value(x0) + value(x1) * d[j];	
		sp = (value(x2) * math.cos((2 * math.pi * d[j]) / 365.25 )) + (value(x3) * math.sin((2 * math.pi * d[j]) / 365.25))
		sc = (value(x4) *  math.cos((2 * math.pi * d[j]) / (365.25 * 10.7))) + (value(x5) * math.sin((2 * math.pi * d[j]) / (365.25 * 10.7)))	
		curvey.append(li + sp + sc);
	pl.plot(d, y, color="green", linewidth=2)
	pl.plot(d, curvey, color="red") 
	pl.show();
	print value(r)
	print value(x0)
	print value(x1)
	print value(x2)
	print value(x3)
	print value(x4)
	print value(x5)
warm_up()
	
