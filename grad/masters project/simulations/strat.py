#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 2 13:19:25 2023

@author: yvan
"""
from matplotlib import pyplot as plt
from math import sqrt
from random import random, seed
from statistics import median


"""
delta t = 1
"""

pm = lambda : 2 * round(random()) - 1
a = 0.01
b = 0.01
#sigma = lambda x : a*x + b
half_a = a/2
update = lambda x, r: ((1 + r*half_a)*x + r*b) / (1 - r*half_a)


versions = 1000
steps = 100000

result = [()]*int(steps / 100)

ten = hundred = thousand = final = ()
for _ in range(versions):
	place = 50
#	result = (place,)
	for i in range(steps):
		place = update(place, pm())
		# place = ( (4 + a**2) * place + a * b + pm() * 2 * ( 2*sigma(place) - b ) ) / ( 4 - a**2 )
		# if place < 0:
		# 	place = - place
		# elif place > 100:
		# 	place = 200 - place
		#result += place,
		if (i % 100) == 0:
			result[int(i * 0.01)] += place,
		match i:
			case 10:
				ten += place,
			case 100:
				hundred += place,
			case 1000:
				thousand += place,
	final += place,

print(sum(1 for i in final if i > 50)/versions)

buckets = list(range(0,100,2)) + [100 + i*10 for i in range(10)]

plt.hist(ten, buckets, histtype = 'step', label = "10 steps", density = True)
plt.hist(hundred, buckets, histtype = 'step', label = "100 steps", density = True)
plt.hist(thousand, buckets, histtype = 'step', label = "1000 steps", density = True)
plt.hist(final, buckets, histtype = 'step', label = str(steps)+" steps", density = True)
plt.legend()
plt.show()

plt.clf()
plt.plot([median(i) for i in result])
plt.show()