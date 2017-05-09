import math

def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)

def nth_number(target_index, data):
        
    if (target_index > fac(len(data))) or (target_index < 1):
        raise ValueError('index should be between {} and {}'.format(1, fac(len(data))))
    
    current_index = 0
    target_number_list = []

    while len(data) != 0:
        n_loop = (target_index - current_index) / fac(len(data)-1)
        
        if str(n_loop).split('.')[1] != '0':
            n_loop = math.floor(n_loop)
        else:
            n_loop = int(n_loop)-1
            
        current_index += fac(len(data)-1) * n_loop
        number = data.pop(n_loop)
        target_number_list.append(number)
        
    final_n = int(''.join([str(x) for x in target_number_list]))
    return final_n

def main():
    target_index = 10**6
    data = [x for x in range(10)]
    print(nth_number(target_index, data))

if __name__ == "__main__":
    main()
