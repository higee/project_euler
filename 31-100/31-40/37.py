def prime_or_not(n):
    
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if not n%i:
            return False
    return True

def truncatable_prime(n):
    
    # check whether given input is a prime number or not
    if not prime_or_not(n):
        return False
    
    # start checking whether truncaed number(s) is(are) also prime number(s)
    str_n = str(n)
    # length should be subtracted by 1 because given number has been checked already
    len_n = len(str_n)-1
    
    for idx in range(len_n):
        truncate_left_to_right = str_n[idx+1:]
        if not prime_or_not(int(truncate_left_to_right)):
            return False       
        truncate_right_to_left = str_n[:len_n-idx]
        if not prime_or_not(int(truncate_right_to_left)):
            return False

    return True

def main():
    
    result = []
    number = 10

    while len(result) != 11:

        if truncatable_prime(number):
            result.append(number)

        number += 1
    
    return sum(result)

if __name__ == "__main__":
    print(main())
