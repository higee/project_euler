def number_letter_counts():

    num1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num2 = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    num3 = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    num4 = ['hundred', 'and']
    num5 = ['thousand'] 

    # 1-99
    g1 = sum([len(x) for x in num1])
    g2 = sum([len(x) for x in num2])
    g3 = sum([len(x) for x in num3])
    g4 = sum([len(x) for x in num3[1:]])*9 + g1*8 

    s1 = g1+g2+g3+g4

    # 100-999
    g_hundred = len(num4[0])
    g_hundred_and = sum([len(x) for x in num4])
    g5 = g1 + g_hundred*9
    g6 = g1*99 + g_hundred_and*9*99 + s1*9

    s2 = g5 + g6

    # 1000
    g7 = len(num1[0]) + len(num5[0])
    s3 = g7

    # total
    total = s1+s2+s3
    return total

def main():
    print(number_letter_counts())

if __name__ == "__main__":
    main()
