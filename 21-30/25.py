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

    def over_n_digits(self, k):
        x = 1
        while len(str(self.__call__(x))) < k:
            x +=1
            if len(str(self.__call__(x))) >= k:
                return x

def main():
    fb = fibo()
    print(fb.over_n_digits(1000))

if __name__ == "__main__":
    main()
