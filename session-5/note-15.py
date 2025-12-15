#!/usr/bin/env python3

students = []

student = {
	'student_code': '40113119821',
	'name': ('saleh','askari'),
	'birth_day': (1382,7,22),
	'course': {
		'AI': {'unit': 3 , 'score':20},
		'DB': {'unit': 3 , 'score':15},
		'QH': {'unit': 2 , 'score':11}
	}
}

students.append(student)

student = {
	'student_code': '40113119822',
	'name': ('alireza','zamani'),
	'birth_day': (1382,10,18),
	'course': {
		'AI': {'unit': 3 , 'score':20},
		'DB': {'unit': 3 , 'score':15},
		'QH': {'unit': 2 , 'score':11},
		'SP': {'unit': 1 , 'score':20}
	}
}

students.append(student)


for i in range(len(students)):
	for key in students[i].keys():
		
		if(key == 'name'):
			print(f'name: {students[i][key][0]}\t family: {students[i][key][1]}')
			continue
		if(key == 'birth_day'):
			print(f'birth day: {students[i][key][0]}/{students[i][key][1]}/{students[i][key][2]}')
			continue
			
		print(f'{key}: {students[i][key]}')
	print('\n------------------------------------------------------\n')