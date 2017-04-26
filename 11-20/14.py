class collatz_seq():
    
    def __init__(self):
        self.data = dict()
        self.data[1] = 1
    
    def __call__(self, max_num):
        previous = 0, 0
        for n in range(1, max_num):
            
            if n in self.data:
                current = int(n), self.data[n]
            else:
                start_n = n
                cnt = 0
                while start_n != 1:
                    if start_n % 2 == 0:
                        start_n = start_n/2
                    else:
                        start_n = (3*start_n)+1
                    cnt += 1
                    if start_n in self.data:
                        cnt += self.data[start_n]
                        break

                self.data[n] = cnt
                current = int(n), cnt
            
            if current[1] > previous[1]:
                previous = current
            else:
                continue
        
        return previous[0]

def main():
    max_num = 10**6
    collatz = collatz_seq()
    print(collatz(max_num))

if __name__ == "__main__":
    main()
