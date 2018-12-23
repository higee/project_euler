def fac(n):    
    
    if n in [0, 1]:
        return 1    
    else:
        return n * fac(n-1)
    
def sum_of_the_factorial_of_their_digits(n):

    fac_of_the_digits = [fac_dic[int(x)] for x in str(n)]
    return sum(fac_of_the_digits)

def main():

    for n in range(10, 2540161):
        if n == sum_of_the_factorial_of_their_digits(n):
            yield n

if __name__ == "__main__":
    global fac_dic 
    fac_dic = {n : fac(n) for n in range(10)}
    answer = list(main())
    print(answer)
