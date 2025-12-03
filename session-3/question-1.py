#!/usr/bin/env python3

while True:
	n = int(input('Enter a number(number > 0): '))
	
	if n > 0:
		break

sum = 0
for i in range(n+1):
	
	if i % 2 == 0:
		sum += i # sum = sum + i
		
print(f'sum: {sum}')