#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 2 13:19:25 2023

@author: yvan
"""
from matplotlib import pyplot as plt
from math import sqrt
from random import random
from statistics import median


"""
delta t = 1
"""

pm = lambda : 2 * round(random()) - 1
a = 0.01
b = 0.01
sigma = lambda x : 1

versions = 100000
steps = 10000

result = [()]*steps

ten = hundred = thousand = final = ()
for v in range(versions):
	place = 50
#	result = (place,)
	for i in range(steps):
		place += pm() * sigma(place)
		# if place < 0:
		# 	place = - place
		# elif place > 100:
		# 	place = 200 - place
		#result[i] += place,
		match i:
			case 10:
				ten += place,
			case 100:
				hundred += place,
			case 1000:
				thousand += place,
	final += place,
	if(v % 1000 == 0):
		print(v)


print(sum(1 for i in final if i > 50)/versions)

buckets = [-140,-110] + list(range(-90,0,10)) + list(range(0,100,2)) + list(range(100,200,10)) + [210,240]


plt.hist(ten, buckets, histtype = 'step', label = "10 steps", density = True)
plt.hist(hundred, buckets, histtype = 'step', label = "100 steps", density = True)
plt.hist(thousand, buckets, histtype = 'step', label = "1000 steps", density = True)
plt.hist(final, buckets, histtype = 'step', label = str(steps)+" steps", density = True)
plt.legend()
plt.show()

plt.clf()
plt.plot([median(i) for i in result if i%10 == 0])
plt.show()