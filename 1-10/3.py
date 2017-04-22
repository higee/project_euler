class prime():
    
    def __init__(self, n):
        self.n = n
        
    def get_factor(self):
        for i in range(2, self.n+1):
            if self.n % i == 0:
                yield i
        #return self.fac
    
    def prime_or_not(self, n):
        for i in range(2, int(n/2)+1):
            if n % i == 0:
                return False
        else:
            return True
    
    def get_prime_factor(self):
        for i in self.get_factor():
            if self.prime_or_not(i):
                yield i
    
    def get_largest_prime_factor(self):
        return max(self.get_prime_factor())

def main():
    n = 600851475143
    p = prime(n)
    p.get_factor()
    p.get_prime_factor()
    print(p.get_largest_prime_factor())

if __name__ == "__main__":
    main()
