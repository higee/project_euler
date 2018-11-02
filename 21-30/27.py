def prime_or_not(n):

    if n < 2:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    else:
        return True

def quadratic_formula(n, a, b):
    
    result = n**2 + a*n + b
    return result

def main():

    max_cnt = 0

    for a in range(-64, 1000, 1):
        for b in range(2, 1001):

            # continue the loop if 'b' is not a prime number
            if not prime_or_not(b):
                continue

            # case when 'b' is a prime number
            else:
                if b==2:
                    # continue the loop if 'a' is an odd number
                    if a % 2:
                        continue
                    # proceed the logic if 'a' is an even number
                    else:
                        # iterate over 'n'
                        n = 0
                        value = quadratic_formula(n, a, b)
                        # while 'value' is a prime number
                        while prime_or_not(value):
                            n += 1
                            value = quadratic_formula(n, a, b)

                        # compare with previous result
                        if n > max_cnt:
                            max_cnt = n
                            max_a, max_b = a, b

                elif b!=2:
                    # proceed the logic if 'a' is an odd number
                    if a % 2:
                        n = 0
                        value = quadratic_formula(n, a, b)

                        while prime_or_not(value):
                            n += 1
                            value = quadratic_formula(n, a, b)

                        if n > max_cnt:
                            max_cnt = n
                            max_a, max_b = a, b

                    # continue the loop if 'a' is an even number
                    else:
                        continue

    answer = max_a * max_b
    return answer

if __name__ == "__main__":
    main()
