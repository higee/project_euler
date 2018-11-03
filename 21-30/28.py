def s_n(n):
    if n < 1:
        raise ValueError('input number should be a positive integer')
    elif n==1:
        return 1
    else:
        a_n = (2*n-1)**2
        b_n = (2*(n-1)-1)**2 + 2*(n-1)
        value = 2*(a_n+b_n)
        
        return value

def main():
    
    result = 0
    for k in range(1, 502):
        result += s_n(k)
    return result

if __name__ == "__main__":
    main()
