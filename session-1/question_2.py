#!/usr/bin/env python3

price = float(input('enter price: '))

tip = float(price * (18/100))
tax = float(price * (7/100))

total = price + tax + tip

print(f'tip: {tip}\ttax: {tax1}\ttotal: {total}')