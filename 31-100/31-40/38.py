def get_pandigital_multiple(n):
    
    tmp_digit_list = []
    multiplicator = 1

    # find pandigital multiples while preserving the instruction
    while (len(set(tmp_digit_list)) == len(tmp_digit_list)) and (len(tmp_digit_list)<9): 

        product = str(n * multiplicator)
        digit_list = list(product)
        tmp_digit_list.extend(digit_list)
        if '0' in tmp_digit_list:
            return False
        multiplicator += 1
    
    # define conditions to be met
    check_length = len(tmp_digit_list) == 9
    check_duplicates = len(set(tmp_digit_list)) == len(tmp_digit_list)
    check_iteration = (multiplicator != 2)

    # if the pandigital multiple found preserves the instruction
    if check_length and check_duplicates and check_iteration:
        result = int(''.join(tmp_digit_list))
        return result
    return False

def main():
    
    # set initial n and pandigital multiple
    n, pandigital_multiple = 9, get_pandigital_multiple(9)

    # continue untill ...
    for p in range(123, 877):
        if ('9' in str(p)) or ('0' in str(p)):
            continue
        N = int('9' + str(p))
        # if there is a pandigital multiple with given input
        if get_pandigital_multiple(N):
            current_pandigital_multiple = get_pandigital_multiple(N)
            # compare with previous pandigital multiple
            if current_pandigital_multiple > pandigital_multiple:
                # replace pandigital_multiple with new pandigital_multiple 
                # when the latter is greater than the former
                pandigital_multiple = current_pandigital_multiple

    return pandigital_multiple

if __name__ == "__main__":
    print(main())