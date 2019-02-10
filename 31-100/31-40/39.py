import math

def main():

    # initialize cnt and p with the values given
    max_cnt, max_p = 3, 10

    for p in range(12, 1001):
        # initialize count every time p gets updated
        cnt = 0
        # c : hypotenuse
        min_c, max_c = round(p/3)+1, p-1

        for c in range(min_c, max_c):

            b_list = []
            a = c-1
            if a+c >= p:
                continue

            while (a not in b_list) and (a > 0):
                b = p-(c+a)
                b_list.append(b)
                
                if c**2 == a**2+b**2:
                    cnt +=1
                    # there exists only one pair of (a, b) per c
                    break

                a -= 1

        # update stats
        if cnt > max_cnt:
            max_cnt = cnt
            max_p = p

    return max_cnt, max_p
    
if __name__ == "__main__":
    print(main())