from string import ascii_uppercase

def get_triangle_number(string):
    
    data = list(string)
    sum_of_indices = sum([char_to_index[key] for key in data])
    
    return sum_of_indices

def get_nth_triangle_number(n):
        
    return int(1/2*n*(n+1))
    

def get_maximum_triangle_number_with_n_character(n):

    k = 2
    triangle_number_candidates = [1]

    largest_alphabet_index = ascii_uppercase.index('Z')+1
    largest_sum_of_alphabet = largest_alphabet_index * n

    while max(triangle_number_candidates) < largest_sum_of_alphabet:
        value = get_nth_triangle_number(k)
        triangle_number_candidates.append(value)
        k += 1
    
    return triangle_number_candidates


def main():

    global char_to_index
    char_to_index = {letter:idx+1 for idx, letter in enumerate(ascii_uppercase)}

    # read file and create a tuple of words
    with open('../../data/p042_words.txt', 'r') as f:
        word_raw = eval(f.read().split()[0])
        word_list = sorted(word_raw, key=len)
    
    max_char_in_word_list = len(word_list[-1])
    triangle_number_candidate_list = get_maximum_triangle_number_with_n_character(max_char_in_word_list)
    answer = sum([1 for word in word_list if get_triangle_number(word) in triangle_number_candidate_list])

    return answer

if __name__ == "__main__":
   print(main())
