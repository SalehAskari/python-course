#!/usr/bin/env python3

n = int(input('enter a number: '))
counter = 1

for i in range(1,n+1):
	for j in range(i):
		print(f'{counter} ' , end = '')
		counter += 1
	print()
	