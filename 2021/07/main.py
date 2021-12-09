from collections import Counter

positions = [int(x) for x in open('inputs.txt').read().split(',')]
min_position = min(positions)
max_position = max(positions)
target_positions = range(min_position,max_position)

position_counter = Counter(positions)

# Part 1
fuel_spent = {}
for x in target_positions:
    fuel = 0
    for z in position_counter.keys():
        fuel += ((abs(z -x)) * position_counter[z])
    fuel_spent[x] = fuel

optimal_position = min(fuel_spent,key=fuel_spent.get)
optimal_fuel = fuel_spent[optimal_position]
print(f"Position:{optimal_position}, Fuel:{optimal_fuel}")


# Part 2
fuel_spent = {}
fuel_cost_index = {}
for x in target_positions:
    fuel = 0
    for z in position_counter.keys():
        distance = abs(z -x)
        if distance not in fuel_cost_index:
            fuel_cost_index[distance] = sum([x for x in range(1,distance+1)])
        fuel+=fuel_cost_index[distance] * position_counter[z]
    fuel_spent[x] = fuel

optimal_position = min(fuel_spent,key=fuel_spent.get)
optimal_fuel = fuel_spent[optimal_position]
print(f"Position:{optimal_position}, Fuel:{optimal_fuel}")
