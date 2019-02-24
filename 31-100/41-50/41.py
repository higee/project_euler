def is_prime(n):
        
    for i in range(2, int(n ** 0.5)+1):
        if not(n%i):
            return False
    return True

def get_previous_pandigital(n):
    
    str_n = str(n)    
    inverse_n = str_n[::-1]
 
    for previous, following in zip(inverse_n[1:], inverse_n):
        if previous > following:
                    
            unchanged = str_n[:str_n.index(previous)]
            to_be_changed = str_n[str_n.index(previous):]            
            to_be_changed_list = sorted(list(to_be_changed), reverse=True)
            
            index = to_be_changed_list.index(previous)+1
            new_key = to_be_changed_list.pop(index)
            
            new_number = int(unchanged + new_key + ''.join(to_be_changed_list))
            
            return new_number
        
    new_number = int(inverse_n[:-1])
    return new_number

def main():

    value = 7654321
    while not is_prime(value):
        value = get_previous_pandigital(value)
    return value

if __name__ == "__main__":
    print(main())
