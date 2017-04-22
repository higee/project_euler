def product_of_three_digit():
    three_digit = range(999, 99, -1)
    for one in three_digit:
        for two in three_digit:
            yield one*two 

class palindrome():
    
    def __init__(self, n):
        self.n = n
    
    def split_number(self):
        self.middle = int(len(str(self.n))/2)
        if len(str(self.n)) % 2 != 0:
            self.from_front = str(self.n)[:self.middle]
            self.from_back = str(self.n)[self.middle+1:][::-1]
        else:
            self.from_front = str(self.n)[:self.middle]
            self.from_back = str(self.n)[self.middle:][::-1]
        return self.from_front, self.from_back
    
    def is_palindrome(self):
        if self.from_front == self.from_back:
            return True
        else:
            False

def main():
    for x in sorted(product_of_three_digit(), reverse=True):
        test = palindrome(x)
        test.split_number()
        if test.is_palindrome():
            print(x)
            break

if __name__ == "__main__":
    main()
