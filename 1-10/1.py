def sum_of_multiples_of_three_or_five(n):
    result = sum([x for x in range(1, n) if x % 3 == 0 or x % 5 == 0])
    return result

def main():
    n = 10**3
    print(sum_of_multiples_of_three_or_five(n))

if __name__ == "__main__":
    main()
