def prime_or_not(n):
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    else:
        return True


def get_first_n_prime(n):
    while True:
        if prime_or_not(n):
            yield n
        n += 1
        
def get_nth_prime_number(n, initial_number=2):
    count = 0
    for next_prime in get_first_n_prime(initial_number):
        count += 1
        if count < n:
            continue
        else:
            return next_prime

def main():
    n = 10001
    print(get_nth_prime_number(n))

if __name__ == "__main__":
    main()
