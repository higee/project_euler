def add_and_square(*args):
    return sum([x for x in args])**2
     
def square_and_add(*args):
    return sum([x**2 for x in args])

def main():
    print(add_and_square(*range(101)) - square_and_add(*range(101)))

if __name__ == "__main__":
    main()
