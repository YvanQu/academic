#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 2 13:19:25 2023

@author: yvan
"""
from matplotlib import pyplot as plt
from math import sqrt
from random import random, seed


"""
delta t = 1
"""

pm = lambda : 2 * round(random()) - 1
a = 1
b = 1
#sigma = lambda x : a*x / (x+b)
update = lambda x, r: (x-b + r*a + sqrt( (x+b)**2 + r*a*(x-b) ))/2

versions = 10000
steps = 100000

ten = hundred = thousand = ten_k = final = ()
for _ in range(versions):
	place = 50
#	result = (place,)
	for i in range(steps):
		place = update(place, pm())
		# place = ( place + a * b + pm() * sigma(place) ) / ( 1 - a**2 )
		if place < 0:
			place = - place
		# elif place > 100:
		# 	place = 200 - place
		#result += place,
		match i:
			case 10:
				ten += place,
			case 100:
				hundred += place,
			case 1000:
				thousand += place,
			case 10000:
				ten_k += place,
	final += place,

buckets = list(range(0,100,2)) + list(range(100,200,20))

plt.hist(ten, buckets, histtype = 'step', label = "10 steps", density = True)
plt.hist(hundred, buckets, histtype = 'step', label = "100 steps", density = True)
plt.hist(thousand, buckets, histtype = 'step', label = "1000 steps", density = True)
plt.hist(ten_k, buckets, histtype = 'step', label = "10000 steps", density = True)
plt.hist(final, buckets, histtype = 'step', label = str(steps)+" steps", density = True)
plt.legend()
plt.show()