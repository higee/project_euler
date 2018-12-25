def prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def check_circular_prime(n):

    str_n = str(n)
    # create a list of rotated numbers
    rotated_numbers = {int(str_n[i:]+str_n[:i]) for i, _ in enumerate(str_n)}

    # when all rotated_numbers are prime numbers
    if all(prime(n) for n in rotated_numbers):
        
        result = {
            'status' : True,
            'total' : len(rotated_numbers),
            'numbers' : rotated_numbers
        }

    else:
        result = {
            'status' : False,
            'numbers' : rotated_numbers
        }

    return result

def main():
    cnt = 0
    check_list = set()

    for i in range(2, 1000000):
        # in case we have only checked the number
        if i in check_list:
            # continue the loop to reduce computation
            continue

        outcome = check_circular_prime(i)
        # if input number is a cicular prime
        if outcome['status']:
            cnt += outcome['total']
        # add rotated numbers to check-list so that we don't have to compute again
        # add both circular and non-circular prime numbers
        # because they are the same in logic
        check_list.update(outcome['numbers'])
    
    return cnt

if __name__ == "__main__":
    print(main())
