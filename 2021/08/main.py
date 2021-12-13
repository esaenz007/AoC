from display import SevenSegmentDisplay

inputs = open('input.txt').read().split('\n')

# Part 1
unique_segs = [2,3,4,7]
count = 0
for x in inputs:
    count += len( [z for z in [len(y) for y in x.split(" | ")[1].split(' ')] if z in unique_segs])
print(count)


# Part 2
part2_solution = 0
display = SevenSegmentDisplay()    

for input in inputs:    
    all_digits = input.split(" | ")[0].split(" ")
    outputs_digits =input.split(" | ")[1].split(" ")

    # Rewire 1
    scrambled_wiring = [d for d in all_digits if len(d)==2][0]
    display.rewire_number(1, scrambled_wiring)
    
    # Rewire 7
    scrambled_wiring = [d for d in all_digits if len(d) == 3][0]
    display.rewire_number(7, scrambled_wiring)

    # Rewire 4
    scrambled_wiring = [d for d in all_digits if len(d) == 4][0]
    display.rewire_number(4, scrambled_wiring)

    # Swap segment 5 & 7 signals until a nine is wired
    for x in [y for y in all_digits if len(y) == 6]:
        if display.get_number(x) == 9:
            break
        display.swap_signals(display.get_segment_signal(5), display.get_segment_signal(7))
        if display.get_number(x) == 9:
            break

    # Solve each output
    output_number = 0
    for i,x in enumerate(reversed(outputs_digits)):
        output_digit = None
        signal_len = len(x)

        # Solve the obvious numbers
        if signal_len == 2:
            output_digit = 1
        elif signal_len == 3:
            output_digit = 7
        elif signal_len == 4:
            output_digit = 4
        elif signal_len == 7:
            output_digit = 8
        
        # If not an obvious number, crack the number by swapping segment 2-4 & segment 3-6 signals until a valid number is wired.
        if output_digit is None:
            output_digit = display.get_number(x)
            if output_digit is None:
                display.swap_signals(display.get_segment_signal(3),display.get_segment_signal(6))
                output_digit = display.get_number(x)
            if output_digit is None:
                display.swap_signals(display.get_segment_signal(2),display.get_segment_signal(4))
                output_digit = display.get_number(x)
            if output_digit is None:
                display.swap_signals(display.get_segment_signal(3),display.get_segment_signal(6))
                output_digit = display.get_number(x)
            if output_digit is None:
                display.swap_signals(display.get_segment_signal(2),display.get_segment_signal(4))
                output_digit = display.get_number(x)

        output_digit = output_digit * pow(10,i)
        output_number += output_digit

    part2_solution += output_number

print(part2_solution)
       