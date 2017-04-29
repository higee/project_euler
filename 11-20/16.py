def sum_of_(n):
    return sum(int(x) for x in list(str(n)))

def main():
    n = 2**1000
    print(sum_of_(n))

if __name__ == "__main__":
    main()
