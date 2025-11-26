#!/usr/bin/env python3

#f(x) = ax^2 + bx + c

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

delta = (b**2) - (4*a*c)

x_1 = (-b + (delta**.5)) / 2 * a
x_2 = (-b - (delta**.5)) / 2 * a

print(f'\n\nf(x) = {a}X^2 + {b}X + {c}\nDELTA: {delta}\nX1: {x_1}\tX2: {x_2}')
