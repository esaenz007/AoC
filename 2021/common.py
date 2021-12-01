
def get_compare_description(val1:int, val2:int):
    if val2 > val1:
        return "increased"
    if val2 < val1:
        return "decreased"
    if val2 == val1:
        return "no change"

def get_depth_change_type_count(depths_list:list, depth_type:str):
    depth_type_count = len([x for x in depths_list if x[1] == depth_type])
    return depth_type_count

def get_inputs(file_name:str,input_type:type=str):
    input_numbers = []

    with open(file_name,'r') as input_file:
        input_numbers = [ input_type(x) for x in input_file.readlines()]

    return input_numbers

def create_running_sum(number_list:list, window_size:int):
    list_size = len(number_list)
    running_sum = [
        sum(number_list[i:i+window_size]) for i, x in enumerate(number_list) if i <= list_size - window_size  
    ]

    return running_sum

def get_value_change_status(values_list:list):
    
    value_change_status = [
        [x, "" if i == 0 else get_compare_description(values_list[i-1], x) ] 
        for i, x in enumerate(values_list)
    ]

    return value_change_status