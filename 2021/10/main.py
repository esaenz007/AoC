import math
inputs = [[y for y in x] for x in open('input.txt').read().split('\n')]

# Day 1
open_chars = ['[','{','<','(']
close_chars = [']','}','>',')']
char_points = {
    ')':3,
    ']':57,
    '}':1197,
    '>':25137
}
char_stack = []
invalid_chars = []
incomplete_lines = []
points = 0
for x in inputs:
    for i,y in enumerate(x):
        if i == 0 and y in close_chars:
            invalid_chars.append(y)
        elif y in open_chars:
            char_stack.append(y)
        elif y in close_chars:
            removed_char = char_stack.pop()
            if removed_char != open_chars[close_chars.index(y)]:
                invalid_chars.append(y)
    if len(invalid_chars) > 0:
        points += sum( [v for k,v in char_points.items() if k in invalid_chars])
    else: 
        # Save incomplete lines for part 2
        incomplete_lines.append(x) 
    invalid_chars.clear()
print(points)


# Day 2
char_stack.clear()
close_stack = []
points_history = []
close_points = {
    ')':1,
    ']':2,
    '}':3,
    '>':4
}
for x in incomplete_lines:
    points = 0
    for y in x:
        if y in open_chars:
            char_stack.append(y)
        elif y in close_chars:
            char_stack.pop()
    
    for y in reversed( char_stack):
        close_stack.append(close_chars[open_chars.index(y)])

    for i, y in enumerate(close_stack):
        points *= 5
        points += close_points[y]

    points_history.append(points)
    char_stack.clear()
    close_stack.clear()


points_history.sort()
print(points_history[ math.floor(len(points_history)/2)])
