class fibo():
    
    def __init__(self):
        self.data = {}
        self.data[0] = 0
        self.data[1] = 1
    
    def __call__(self, n):
        if n in self.data:
            return self.data[n]
        else:
            result = self.__call__(n-1) + self.__call__(n-2)
            self.data[n] = result
            return result

def sum_of_the_even_valued_term(n=0):
    fi = fibo()
    while fi(n) < 4000000:
        n += 1
        if fi(n) > 4000000:
            del fi.data[n]
            values = list(fi.data.values())
            even_values = [x for x in values if x % 2 == 0]
            sum_of_the_even_valued_term = sum(even_values)
            return sum_of_the_even_valued_term

def main():
    print(sum_of_the_even_valued_term())

if __name__ == "__main__":
    main()
