import functools

def greatest_common_denominator(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

def least_common_multiple(a, b):
    if any(x <= 0 for x in [a, b]):
        return 'positive numbers only'
    return a * b // greatest_common_denominator(a, b)

def least_common_multiple_(*args):
    if any(x <= 0 for x in args):
        return 'positive numbers only'
    return functools.reduce(least_common_multiple, args)

def main():
    print(least_common_multiple_(*(range(1, 21))))

if __name__ == "__main__":
    main()
