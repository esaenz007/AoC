from graph import LineChart

# Load line coordinates into memory
all_lines = [ x.split(" -> ") for x in open("inputs.txt").read().split("\n")]
all_lines = [[y.split(",") for y in x] for x in all_lines]
all_lines = [[[int(z) for z in y] for y in x] for x in all_lines]

# Part 1
line_chart = LineChart(1000, 1000)
horizontals_verticals_only = [x for x in all_lines if x[0][0] == x[1][0] or x[0][1] == x[1][1]]
for i, x in enumerate( horizontals_verticals_only):
    line_chart.draw_line(x[0][0], x[0][1], x[1][0], x[1][1])

#print("Line chart:")
#line_chart.print_chart()
#print()
print(f"Solution:{line_chart.get_dangerous_point_count()}")


# Part 2
line_chart = LineChart(1000, 1000)
for i, x in enumerate( all_lines):
    line_chart.draw_line(x[0][0], x[0][1], x[1][0], x[1][1])

# print("Line chart:")
# line_chart.print_chart()
# print()
print(f"Solution:{line_chart.get_dangerous_point_count()}")
