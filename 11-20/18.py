def preprocess(data):
    result = []
    for item in data.lstrip().rstrip().split('\n'):
        each_result = []
        for each in item.split(' '):
            each_result.append(int(each))
        result.append(each_result)
    result.reverse()
    return result

def reduce_list(data):
    reduced_list = []
    for a, b in zip(data, data[1:]):
        if a < b:
            reduced_list.append(b)
        else:
            reduced_list.append(a)
    return reduced_list

def add_lists(data1, data2):
    return [sum(x) for x in zip(data1, data2)]

def maximum_path(data):
    for index, row in enumerate(data):
        first_row = reduce_list(row)
        added_row = add_lists(first_row, data[index+1])
        index += 1

        while index+1 != len(data):
            reduced_row = reduce_list(added_row)
            added_row = add_lists(reduced_row, data[index+1])
            index += 1

        return added_row

def main():
     
    data ="""
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

    print(maximum_path(preprocess(data))[0])

if __name__ == "__main__":
    main()
