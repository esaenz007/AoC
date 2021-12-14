inputs = [[int(y) for y in x] for x in open('input.txt').read().split('\n')]

#Part 1
low_points = []
x = 0
y = 0
up = -1
down = 1
left = -1
right = 1
for y, row in enumerate(inputs):
    for x, cell in enumerate(row):
        # Check top
        if y+up >= 0:
            if cell >= inputs[y+up][x]:
                continue
        # Check right
        if x+right < len(row):
            if cell >= inputs[y][x+right]:
                continue
        # Check bottom
        if y+down < len(inputs):
            if cell >= inputs[y+down][x]:
                continue
        # Check left
        if x+left >= 0:
            if cell >= inputs[y][x+left]:
                continue
        low_points.append([x,y])

low_point_levels = [inputs[x[1]][x[0]] for x in low_points]
print(sum([x+1 for x in low_point_levels]))


# Part 2
def calc_basins(matrix,x,y):
    basin_index = {
        f"{x}{y}":0    
    }
    current_level = matrix[y][x]
    up = -1
    down = 1
    right = 1
    left = -1
    # Check top
    if y+up >= 0:
        neighbor = matrix[y+up][x]
        if neighbor > current_level and neighbor < 9:
            basin_index = {**basin_index, **calc_basins(matrix,x,y+up)}
    # Check right
    if x+right < len(matrix[y]):
        neighbor = matrix[y][x+right]
        if neighbor > current_level and neighbor < 9:
            basin_index = {**basin_index, **calc_basins(matrix,x+right,y)}
    # Check bottom
    if y+down < len(matrix):
        neighbor = matrix[y+down][x]
        if neighbor > current_level and neighbor < 9:
            basin_index = {**basin_index, **calc_basins(matrix,x,y+down)}
    # Check left
    if x+left >= 0:
        neighbor = matrix[y][x+left]
        if neighbor > current_level  and  neighbor < 9:
            basin_index = {**basin_index, **calc_basins(matrix,x+left,y)}

    return basin_index

basin_sizes = [len(calc_basins(inputs, z[0], z[1])) for z in low_points]
basin_sizes.sort(reverse=True)
print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2] )