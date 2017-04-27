def fac(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def main():
    answer =  fac(40)/(fac(20)*fac(20))
    return answer

if __name__ == "__main__":
    print(main())
