import functools

class factorial_digit_sum():
    
    def fac(self, n):
        self.n = n
        
        if self.n == 0:
            return 1
        else:
            return self.n * self.fac(n-1)

    def __call__(self, n):
        digit_in_fac_in_list = list(str(factorial_digit_sum.fac(self, n)))
        return functools.reduce(lambda x, y: int(x)+int(y), digit_in_fac_in_list)

def main():
    euler_20 = factorial_digit_sum()
    n = 100
    print(euler_20(n))

if __name__ == "__main__":
    main()
