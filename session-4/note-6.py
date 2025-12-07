#!/usr/bin/env python3

score = [12,18,17,18,18]

print(score)

score.insert(1,20)

score.append(10)

print(score)

score.remove(18)

print(score)

score.sort()

score.reverse()

print(f'Sorted(reverse): {score}')

score.clear()

print(score)

#print(f'Remove Item: {removeItem}')