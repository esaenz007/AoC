inputs = open('inputs.txt').read().split('\n')
folds = [[x.replace("fold along ","").split("=")[0],int(x.replace("fold along ","").split("=")[1])]for x in inputs[inputs.index("")+1:]]
dots = [[int(y) for y in x.split(",")] for x in inputs[0:inputs.index("")]]

# Rotate paper clockwise specified number of times
def rotate(paper,count=1):
    for x in range(count):
        paper = list(zip(*paper[::-1]))

    return [list(x) for x in paper]

# Merge dots for two papers
def merge_dots(paper1,paper2):
    larger = paper1 if len(paper1)>=len(paper2) else paper2
    smaller = paper2 if len(paper2)<=len(paper1) else paper1
    larger = list(reversed(larger))

    for yi,y in enumerate(smaller):
        for xi, x in enumerate(y):
            if x == "#":
                larger[yi][xi] = x
    return list(reversed(larger))

# Fold paper up
def fold_up(paper,line):
    top = paper[0:line]
    bottom = paper[line+1:]
    return merge_dots(top, bottom)

def fold_down(paper,line):

    return paper

def print_paper(paper):
    for x in paper:
        print(''.join(x))

def count_dots(paper):
    count = 0
    for y in paper:
        for x in y:
            if x == "#":
                count += 1
    return count

width = max(x[0] for x in dots)+1
height = max(x[1] for x in dots)+1

paper = [[' ' for y in range(width)] for x in range(height)]

for x in dots:
    paper[x[1]][x[0]] = '#'

for i,x in enumerate(folds):
    
    if x[0] == "x":
        paper = rotate(paper, 1)
    
    paper = fold_up(paper, x[1])

    if x[0] == "x":
        paper = rotate(paper, 3)

    if i == 0:
        print(count_dots(paper))

print_paper(paper)
print("")
