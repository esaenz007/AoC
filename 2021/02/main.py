import sys
sys.setrecursionlimit(1500)# Increase max recustion limit

directions = open("inputs_test.csv").read().split("\n") # Credit to Alex Lach for simple one liner file reader

# Part 1
# Recursive function returns horz position and depth based on list of directions
def calc_position(directions:list, curr_depth:int=0, curr_horz_position:int=0, curr_direction_index=0):
    
    if curr_direction_index < len(directions):
        curr_direction = directions[curr_direction_index].split(" ")

        if curr_direction[0] == "forward":
            curr_horz_position += int(curr_direction[1])
        elif curr_direction[0] == "down":
            curr_depth += int(curr_direction[1])
        elif curr_direction[0] == "up":
            curr_depth -= int(curr_direction[1])
        
        curr_direction_index+=1 # Move to next direction
        
        return calc_position(directions,curr_depth=curr_depth,curr_horz_position=curr_horz_position,curr_direction_index=curr_direction_index)
    else:
        return curr_depth, curr_horz_position

# Calculate horz position & total depth
horizontal_position, total_depth = calc_position(directions)
print(f"Horizontal Position: {horizontal_position}, Depth: {total_depth}, Product: {total_depth*horizontal_position}")


# Part 2
# Recursive function returns horz position and depth based on list of directions.  Implements aim.
def calc_position(directions:list, curr_depth:int=0, curr_horz_position:int=0, curr_aim=0, curr_direction_index=0):
    
    if curr_direction_index < len(directions):
        curr_direction = directions[curr_direction_index].split(" ")

        if curr_direction[0] == "forward":
            curr_horz_position += int(curr_direction[1])
            curr_depth +=  curr_aim * int(curr_direction[1])
        elif curr_direction[0] == "down":
            curr_aim += int(curr_direction[1])
        elif curr_direction[0] == "up":
            curr_aim -= int(curr_direction[1])
        
        curr_direction_index+=1 # Move to next direction

        return calc_position(directions,curr_depth=curr_depth,curr_horz_position=curr_horz_position,curr_aim=curr_aim,curr_direction_index=curr_direction_index)
    else:
        return curr_horz_position, curr_depth

# Calculate horz position & total depth
horizontal_position, total_depth = calc_position(directions)
print(f"Horizontal Position: {horizontal_position}, Depth: {total_depth}, Product: {total_depth*horizontal_position}")