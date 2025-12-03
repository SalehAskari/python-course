#!/usr/bin/env python3

n = int(input('enter a number: ')) # n = 5
space = n - 1 # space = 4

for i in range(1,n+1):
	for j in range(space):
		print(' ' , end = '')
	space -=1
	
	
	for k in range(i):
		print('* ' , end = '')
	print()