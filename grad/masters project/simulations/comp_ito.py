#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 2 13:19:25 2023

@author: yvan
"""
from matplotlib import pyplot as plt
from math import sqrt
from random import random


"""
delta t = 1
"""

pm = lambda : 2 * round(random()) - 1
b = 1
a = 100
sigma1 = lambda x : b*x / (x + 1)
sigma2 = lambda x : b*x / (x + a)

versions = 1
steps = 100000

ten = hundred = thousand = ten_k = final = ()
for _ in range(versions):
	place = place1 = place2 = 50
	result1 = result2 = (place,)
	for i in range(steps):
		p = pm()
		place1 += p * sigma1(place1)
		place2 += p * sigma2(place2)
		# if place < 0:
		# 	place = - place
		# elif place > 100:
		# 	place = 200 - place
		result1 += place1,
		result2 += place2,
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

buckets = list(range(0,100,2)) + list(range(100,150,10))

plt.hist(ten, buckets, histtype = 'step', label = "10 steps", density = True)
plt.hist(hundred, buckets, histtype = 'step', label = "100 steps", density = True)
plt.hist(thousand, buckets, histtype = 'step', label = "1000 steps", density = True)
plt.hist(ten_k, buckets, histtype = 'step', label = "10000 steps", density = True)
plt.hist(final, buckets, histtype = 'step', label = str(steps)+" steps", density = True)


plt.legend()
plt.show()
plt.clf()

plt.plot(result1,label="a=1")
plt.plot(result2,label="a=100")
plt.legend()
plt.show()