def get_number_of_elements(group_idx):

    number_of_elements_in_group = 10**(group_idx)-10**(group_idx-1)
    length_of_each_number = group_idx

    return number_of_elements_in_group * length_of_each_number

def get_group_idx(n):

    # set initial value
    total_number_of_elements = get_number_of_elements(1)
    group_idx = 1

    # filter out cases when n belongs to the first group
    if n < total_number_of_elements:
        return group_idx
    # iterate over till group to which n belongs is found
    while n > total_number_of_elements:
        group_idx +=1
        total_number_of_elements += get_number_of_elements(group_idx)

    return group_idx


def get_idx_within_group(n):

    # get group idx first    
    group_idx = get_group_idx(n)
    # get idx within above group
    accumulated_number_of_elements = sum([get_number_of_elements(idx) for idx in range(1, group_idx)])
    idx_within_group = n-accumulated_number_of_elements 

    return idx_within_group

def get_value(n):

    group_idx = get_group_idx(n)
    idx_within_group = get_idx_within_group(n)

    group_idx_within_group = ((idx_within_group-1)//(group_idx))+1
    element_idx_within_group_in_group = (idx_within_group-1)%(group_idx)

    # find first value in each group
    # i.e. in group 2, first value is 10
    first_value_in_group = 10**(group_idx-1)
    value = str(first_value_in_group + (group_idx_within_group-1))*1
    value = int(value[element_idx_within_group_in_group])
    
    return value

def main():
    
    candidates  = [10**x for x in range(7)]
    answer = 1
    
    for candidate in candidates:
        answer *= get_value(candidate)
    return answer

if __name__ == "__main__":
    print(main())