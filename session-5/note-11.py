#!/usr/bin/env python3


l = [True , 12,'hello',12.89,[23,'world']]
print(l)
l[0] = False
print(l)

print('-----------------Tuple')
t = ('saleh','askari',23)
print(type(t))
t = list(t)
print(type(t))
t[0] = 'ahmad'
t = tuple(t)
print(type(t))
print(t)
