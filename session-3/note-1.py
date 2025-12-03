#!/usr/bin/env python3
enter = int(input('enter a integer number: ')) # enter = 1234


while enter != 0: # entre = 0 False count = 4
	number = enter % 10 # number = 1 enter = 1
	enter = int(enter / 10) # enter = 0
	
	print(number)
	
print('Finish!')

