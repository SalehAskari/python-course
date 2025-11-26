#!/usr/bin/env python3

numberOfCooki = int(input('enter number of cooki: '))

suger = 1.5
butter = 1
flour = 2.75


suger_needed = (numberOfCooki / 48) * suger
butter_needed = (numberOfCooki / 48) * butter
flour_needed = (numberOfCooki / 48) * flour

print(f'number of cookie: {numberOfCooki}\nsuger: {suger_needed}\nbutter: {butter_needed}\nflour: {flour_needed}')

