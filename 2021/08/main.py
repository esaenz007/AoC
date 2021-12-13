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
for out in inputs:
    display = SevenSegmentDisplay()    
    all_digits = out.split(" | ")[0].split(" ")
    outputs_digits =out.split(" | ")[1].split(" ")

    # Rewire 1
    scrambled_wiring = [d for d in all_digits if len(d)==2][0]
    display.rewire_number(1, scrambled_wiring)
    
    # Rewire 7
    scrambled_wiring = [d for d in all_digits if len(d) == 3][0]
    display.rewire_number(7, scrambled_wiring)

    # Rewire 4
    scrambled_wiring = [d for d in all_digits if len(d) == 4][0]
    display.rewire_number(4, scrambled_wiring)

    # Find & rewire 9
    nine_signals = display.get_signals(9)
    seg_7_sig = display.get_segment_signal(7)
    nine_signals = list(set(nine_signals) - set(seg_7_sig))
    for x in [y for y in all_digits if len(y) == 6]:
        missing_signal = list(set(x)-set(nine_signals))
        if len(missing_signal) == 1:
            display.rewire_number(9, x)
            break

    # Solve each output
    number = 0
    for i,x in enumerate(reversed(outputs_digits)):
        output_digit = None
        signal_len = len(x)
        if signal_len == 2:
            output_digit = 1
        elif signal_len == 3:
            output_digit = 7
        elif signal_len == 4:
            output_digit = 4
        elif signal_len == 7:
            output_digit = 8
        else:
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

        if output_digit is None:
            print(f"Could not crack {x}")
            exit()
        output_digit = output_digit * pow(10,i)
        number += output_digit
    part2_solution += number

print(part2_solution)
       