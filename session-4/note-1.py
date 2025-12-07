enter = input() #he2llo
result = '' # result = ''

for i in range(len(enter)):
	#print(enter[i],ord(enter[i]))
	if ord(enter[i]) < 48 or ord(enter[i]) > 57: # enter[2] = 2
		result += enter[i] # result = 'he'
		
print(result)

