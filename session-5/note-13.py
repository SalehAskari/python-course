#!/usr/bin/env python3

d = {'name': 'saleh',
	'family': 'askari',
	'birth_day': (1382,7,22)}

for key in d.keys():
	print(f'{key} -> {d[key]}')