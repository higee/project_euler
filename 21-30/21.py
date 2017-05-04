class amicable():
        
    def d(self, n):
        
        if n == 1:
            return 0

        else:
            sum_of_factors = 0
            for i in range(1, int(n**0.5)+1):
                if n % i == 0:
                    sum_of_factors += i
                    if n/i != n:
                        sum_of_factors += int(n/i)

        return sum_of_factors
    
    def __call__(self, n):
        
        sum_of_amicable = 0
        
        for i in range(1, n):

            original = i, amicable.d(self, i)
            inverse = amicable.d(self, amicable.d(self, i)), amicable.d(self, i)

            if (original == inverse) & (amicable.d(self, i) != i):
                sum_of_amicable += i

        return sum_of_amicable

def main():
    euler_21 = amicable()
    n=10000
    print(euler_21(n))

if __name__ == "__main__":
    main()
