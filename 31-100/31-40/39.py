import math

def main():

    max_sum_of_two_sides = 600
    duplicate_check_list = []
    cnt_list = []

    for a in range(1, max_sum_of_two_sides):
        for b in range(1, max_sum_of_two_sides-a):
            c = math.sqrt(a**2+b**2)
            if c.is_integer():
                c = int(c)
                p = a+b+c
                if p <= 1000:
                    sorted_sides_of_triangle = sorted((a, b, c))
                    if sorted_sides_of_triangle in duplicate_check_list:
                        continue
                    else:
                        cnt_list.append(p)
                        duplicate_check_list.append(sorted_sides_of_triangle)
            else:
                continue
    
    result = dict((perimeter, cnt_list.count(perimeter)) for perimeter in set(cnt_list))
    answer = max(result, key=lambda x: result[x])    

    return answer

if __name__ == "__main__":
    print(main())