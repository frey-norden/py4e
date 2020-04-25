#!/usr/bin/env python3
# File: countingpattern.py

counts = dict()
print('Type me up some text, real fast! From chicken filet:')
line = input('')

words = line.split()

print('Words:', words)

print('Runnin a count real quick...hold up.')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)

for key in counts:
    print(key, counts[key])

funksters = {'george' : 1, 'bootsy' : 22, 'eddie' : 44}
print(list(funksters))
print(funksters.keys())
print(funksters.values())
print(funksters.items())
