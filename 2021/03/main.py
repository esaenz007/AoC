
# Converts list of bits to decimal value
def bit_list_to_dec(bit_list):
    return int("".join(str(x) for x in bit_list),2)

inputs = [x for x in open('input.csv').read().split("\n")]

#Part 1
# Sum up bits in each col
bit_sums = [0 for x in range(len(inputs[0]))]
for x in inputs:
    for i, y in enumerate(x):
        bit_sums[i] += int(y)

#Calculate gama & epsilon rates
gama_rate = [1 if x >= len(inputs)/2 else 0 for x in bit_sums]
epsilon_rate = [int(not x) for x in gama_rate]

#Conver to decimal
gama_rate_dec = bit_list_to_dec(gama_rate)
epsilon_rate_dec = bit_list_to_dec(epsilon_rate)

#Calculate power consumption
power_consumption = gama_rate_dec * epsilon_rate_dec
print(power_consumption)


# Part 2
def filter(inputs,filter_type,col=0):
    if filter_type == "oxy":
        x_common = 1 if sum([int(x[col]) for x in inputs]) >= len(inputs)/2 else 0
    elif filter_type == "co2":
        x_common = 1 if sum([int(x[col]) for x in inputs]) < len(inputs)/2 else 0

    filterd_inputs = [x for x in inputs if int(x[col]) == x_common]
    
    if len(filterd_inputs) == 1:
        return filterd_inputs[0]
    else:
        col += 1
        return filter(filterd_inputs,filter_type,col=col)

# Calculate oxy & co2 rates    
oxy = bit_list_to_dec(filter(inputs,"oxy"))
co2 = bit_list_to_dec(filter(inputs,"co2"))

#Calculate life support rate
print(oxy * co2)
