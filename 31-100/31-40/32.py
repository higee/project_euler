numbers = range(1, 10)

def prime_or_not(n):
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    else:
        return True

def product_candidates_with_n_digit(n):

    minimum = 10**(n-1)
    maximum = 10**n
    
    tmp_result = range(minimum, maximum)
    final_result = [x for x in tmp_result if (not prime_or_not(x) and not '0' in str(x) and len(set(str(x))) == n)]
    
    return final_result

def validate_pandigital_product(n):
        
    # list of numbers excluding 'n'
    numbers_excluding_n = [x for x in numbers if str(x) not in str(n)]
    
    # when multiplicand is 1-digit or 4-digit number
    for multiplicand in numbers_excluding_n:
        
        sorted_multiplier_list = sorted([str(x) for x in numbers_excluding_n if str(x) not in str(multiplicand)])
        
        # if 'n' is not divisible skip this iteration
        if n % multiplicand != 0:
            continue
        
        # if 'n' is divisible
        quotient = str(int(n/multiplicand))
        sorted_quotient = sorted(quotient)
                
        if sorted_quotient == sorted_multiplier_list:
            return n
    
    # when multiplicand is 2-digit or 3-digit number
    multiplicand_list = [(int(x),int(y)) for x in numbers_excluding_n for y in numbers_excluding_n if x!=y]
    for multiplicand_pair in multiplicand_list:
        multiplicand = int(''.join([str(x) for x in multiplicand_pair]))
                
        # if 'n' is not divisible skip this iteration
        if n % multiplicand != 0:
            continue
        
        # if 'n' is divisible
        quotient = str(int(n/multiplicand))
        sorted_quotient = sorted(quotient)
        sorted_multiplier_list = sorted([str(x) for x in numbers_excluding_n if str(x) not in str(multiplicand)])
        
        if sorted_quotient == sorted_multiplier_list:
            return n

def main():
    pandigital_products = 0
    # product could only be 4-digit numbers
    candidates = product_candidates_with_n_digit(4)
    for candidate in candidates:
        if validate_pandigital_product(candidate):
            pandigital_products += candidate
    
    print(pandigital_products)
    return pandigital_products

if __name__ == "__main__":
    main()
