#!/usr/bin/env python3
score = []

while True:
	enter = int(input('Enter a Score(enter -1 to end): '))
	
	if enter == -1:
		break
	
	score.append(enter)
	
print(f'Score: {score}')