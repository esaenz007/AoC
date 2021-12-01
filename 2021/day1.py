from common import get_compare_description, get_inputs, create_running_sum, get_value_change_status, get_depth_change_type_count

# Inputs file name
inputs_file_name = "inputs.csv"
# Runing sum window size
window_size = 1
# What depth change typs to summarize
depth_change_types_to_summarize = ["increased","decreased","no change"]

# Holds inputs in memory
input_lines = []

# Get inputs 
input_lines = get_inputs(inputs_file_name,input_type=int)

# Create running sum
input_lines_running_sum = create_running_sum(input_lines,window_size)

# Add change status
input_lines_with_report = get_value_change_status(input_lines_running_sum)

# Count depths changed types
print("Depth change counts:")
for x in depth_change_types_to_summarize:
    change_type_count = get_depth_change_type_count(input_lines_with_report, x)
    print(f"\t - {x} = {change_type_count}")
print(f"\t - total = {len(input_lines_with_report)-1}")
