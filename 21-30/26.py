def recursive_division(numberator, denominator):

    # divide by denominator
    x = numberator//denominator

    # while divisible by denominator
    while not x % denominator:
        x //= denominator
        
    return x

def is_recurring_decimal(n):
    
    if n < 1:
        raise ValueError('{n} must be greater than or equal to 1')
        
    x = n/2
    y = n/5

    # if divisible by 2
    if x.is_integer():
        divide_by_two = recursive_division(numberator=n, denominator=2)
        # if completely divisible by 2
        if divide_by_two == 1:
            return False
        
        else:
            # if divisible by 2 and 5
            x = divide_by_two/5
            if x.is_integer():
                divide_by_five = recursive_division(numberator=divide_by_two, denominator=5)
                # if completely divisible by 2 and 5
                if divide_by_five == 1:
                    return False
                else:
                    return True
    
            # if contains factors other than 2 
            else:
                return True

    # if divisible only by 5
    elif y.is_integer():
        divide_by_five = recursive_division(numberator=n, denominator=5)
        if divide_by_five == 1:
            return False
        else:
            return True 

    elif n == 1:
        return False

    # not divisible either by 2 or 5
    else:
        return True

def find_length(n):
    x = 1
    
    r_list = []
    r = x * 10 % n 
    
    # repeat until same remainder appears
    while r not in r_list:
        r_list.append(r)
        r = r * 10 % n

    return len(r_list)

def main():
    previous = 0, 0
    for i in range(1, 1000):
        if is_recurring_decimal(i):
            current = i, find_length(i)
            if current[1] > previous[1]:
                previous = current
            else:
                continue

    print(previous[0])
    return previous[0]

if __name__ == "__main__":
    main()
