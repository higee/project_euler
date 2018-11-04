from collections import Counter

def total():

    a = range(2, 101)
    b = range(2, 101)

    number_of_integer_combinations = len(a) * len(b)

    return number_of_integer_combinations

def dup_2():

    p = [2**a for a in range(2, 101)]
    q = [4**a for a in range(2, 101)]
    r = [8**a for a in range(2, 101)]
    s = [16**a for a in range(2, 101)]
    t = [32**a for a in range(2, 101)]
    u = [64**a for a in range(2, 101)]

    result = dict(Counter(p + q + r + s + t + u))
    result = [v for _, v in result.items() if v > 1]

    number_of_duplicates = sum([v-1 for v in result])

    return number_of_duplicates

def dup_3():

    x = [3**a for a in range(2, 101)]
    y = [9**a for a in range(2, 101)]
    z = [27**a for a in range(2, 101)]
    w = [81**a for a in range(2, 101)]

    result = dict(Counter(x + y + z + w))
    result = [v for _, v in result.items() if v > 1]

    number_of_duplicates = sum([v-1 for v in result])

    return number_of_duplicates

def dup_rest():

    superscript = 4
    cnt = 0

    while superscript <= 100:

        superscript += 2
        cnt += 1

    return cnt

def main():

    answer = total() - (dup_2() + dup_3() + 4*dup_rest())
    return answer

if __name__ == "__main__":
    main()
