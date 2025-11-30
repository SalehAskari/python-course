#!/usr/bin/env python3

side_a = int(input())
side_b = int(input())
side_c = int(input())


if (side_a + side_b > side_c) and (side_a + side_c > side_b) and (side_b + side_c > side_a):
	if side_a == side_b and side_a == side_c:
		print('Equilateral')
	elif (side_a == side_b) or (side_a == side_c) or (side_b == side_c):
		print('Isosceles')
	else:
		print('Scalene')

	
		
else:
	print('no')
	