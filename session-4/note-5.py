#!/usr/bin/env python3

score = [18,19,15,12,11,10,9,16]

min = 20
max = 0

sum = 0
for item in score: #item = 18
	print(f'Item: {item} ,Sum: {sum}')
	sum += item
	
	if min > item:
		min = item # min = 9
	if max < item:
		max = item # max = 19
avrage = sum / len(score)
print(f'SumFinal: {sum} \t Avrage: {avrage}')
print(f'Min: {min} \t Max:{max}')