class palindrome():
    
    def __init__(self, n):
        self.n = n
    
    def split_number(self):
        
        middle = int(len(str(self.n))/2)
        
        # in case 'n' is an odd digit number (one-digit, three-digit, ...) 
        if len(str(self.n))%2:
            self.from_front = str(self.n)[:middle]
            self.from_back = str(self.n)[middle+1:][::-1]

        # in case 'n' is an even digit number (two-digit, four-digit, ...) 
        else:
            self.from_front = str(self.n)[:middle]
            self.from_back = str(self.n)[middle:][::-1]
                
    def is_palindrome(self):
        if self.from_front == self.from_back:
            return True
        return False

class binary():
    
    def __init__(self):
        self.binary = ''
    
    def convert_to_binary(self, n):
        
        quotient, remainder = str(int(n/2)), str(n%2)
        
        # keep dividing until quotient becomes too small
        if quotient in ['0', '1']:
            self.binary = quotient + remainder + self.binary
            return int(self.binary)

        self.binary = remainder + self.binary
        return self.convert_to_binary(int(quotient))

def main():

    result = []
    for number in range(1, int(10e+5)):

        # even decimal-number cannot be panlindromic in binary-number format
        if not number%2:
            continue
        
        # create a palindrome object with given input number
        decimal_palindrom_object = palindrome(number)
        decimal_palindrom_object.split_number()
        
        # if input number is a palindromic decimal number
        if decimal_palindrom_object.is_palindrome():
            
            # create a binary object
            binary_number_object = binary()
            # convert decimal number to binary number
            binary_number = binary_number_object.convert_to_binary(number)
            # create a palindrome object with converted binary number
            binary_palindrom_object = palindrome(binary_number)
            binary_palindrom_object.split_number()
            if binary_palindrom_object.is_palindrome():
                result.append(number)
    
    return sum(result)

if __name__ == "__main__":
    print(main())
