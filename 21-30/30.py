def sum_of_fifth_power(k):

    value = str(k)
    value_split = list(value)
    sum_of_fifth_power_of_value = sum([int(x)**5 for x in value_split])
    
    return sum_of_fifth_power_of_value

def main():
    
    result = 0
    for i in range(2, int(10e5)):
        if i == sum_of_fifth_power(i):
            result += i
    
    return result

if __name__ == "__main__":
    main()
