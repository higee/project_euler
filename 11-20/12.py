def count_factor(n, factor=0):
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            factor += 2
    return factor

def nth_triangular_number(n):
    return int(n+(n*(n-1))/2)

def find_triangular_number_over(k, n=0):
    while count_factor(nth_triangular_number(n)) <= k:
        n += 1
    return nth_triangular_number(n)

def main():
    print(find_triangular_number_over(500))

if __name__ == "__main__":
    main()
