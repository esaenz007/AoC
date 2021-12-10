inputs = [x.split(' | ')[1] for x in open('input.txt').read().split('\n')]

# Part 1
unique_segs = [2,3,4,7]
count = 0
for x in inputs:
    count += len( [z for z in [len(y) for y in x.split(' ')] if z in unique_segs])

print(count)