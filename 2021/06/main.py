
import asyncio
import math
import time
import asyncio
import concurrent.futures
from collections import Counter
    
input_file_name:str = "inputs.txt"
fish = [int(x) for x in open(input_file_name).read().split(',')]

# Part 1 80 days
part1_fish = fish.copy()
for x in range(80): 
    new_borns = []
    fish_index = 0
    for y in part1_fish:
        if y == 0:
            part1_fish[fish_index] = 6
            new_borns.append(8)
        else:
            part1_fish[fish_index] -= 1
        fish_index += 1
    part1_fish = part1_fish + new_borns
print(len(part1_fish))



# Part 2 256 days
count = 0
fish_counts = dict(Counter(fish))
for x in range(256):
    new_counts = {x:0 for x in range(9)}
    for y in fish_counts:
        if y == 0:
            new_counts[8] = fish_counts[y]
            new_counts[6] = fish_counts[y]
        else:
            new_counts[y-1] += fish_counts[y]
    fish_counts = new_counts
print(sum(fish_counts.values()))


# Multiprocess brute force attempt failed miserably

# def count_offspring(initial_state,num_of_days):
#     num_of_offspring=0
#     for x in range(num_of_days):
#         if initial_state==0:
#             initial_state=6
#             num_of_offspring += ( count_offspring(8, num_of_days-x-1) + 1)
#         else:
#             initial_state -= 1
#     return num_of_offspring
#
# with concurrent.futures.ProcessPoolExecutor() as executor:
#     futures = [executor.submit(count_offspring,x, 256) for x in fish]
#     done,pending = concurrent.futures.wait(futures,return_when=concurrent.futures.ALL_COMPLETED)
#     count += sum([x.result() for x in done])
# print(count + len(fish))

