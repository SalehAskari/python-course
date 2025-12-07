#!/usr/bin/env python3

# saleh askari => SAsk
name = input('Name: ')
family = input('Family: ')

username = name[0].upper() + family[0].upper() + family[1:3]

print(f'UserName: {username}')