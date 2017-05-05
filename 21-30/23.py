class abundant_number():
    
    def abundant_or_not(self, n):
        
        sum_of_fac = 0
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                sum_of_fac += i

                if (n/i != n) & (n/i != i):
                    sum_of_fac += n/i

        if sum_of_fac > n:
            return 'abundant number'

    def listify_the_sum_of_two_abundant_numbers(self, n):
        
        abundant_numbers = []
        for i in range(1, n):
            if abundant_number.abundant_or_not(self, i) == 'abundant number':
                abundant_numbers.append(i)

        self.sum_of_two = set()
        
        for x1 in abundant_numbers:
            for x2 in abundant_numbers:
                if x1+x2 not in self.sum_of_two:
                    self.sum_of_two.add(x1+x2)

        return self.sum_of_two
    
    def __call__(self, n):

        result = 0
        for x in range(1, n):
            if x not in self.sum_of_two:
                result += x

        return result

def main():
    euler_23 = abundant_number()
    euler_23.listify_the_sum_of_two_abundant_numbers(28124)
    print(euler_23(28124))

if __name__ == "__main__":
    main()
