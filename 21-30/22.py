import string

class names_scores():
    
    def __init__(self):
        alphabet = string.ascii_lowercase
        self.alpha_dict = dict()
        for index, value in enumerate(alphabet, 1):
            self.alpha_dict[value] = index
    
    def read_file(self):
        with open('../data/p022_names.txt', 'r') as f:
            names = f.read()
            self.name_list = [x[1:-1] for x in names.split(",")]
            self.name_list.sort(reverse=False)
    
    def __call__(self):
    
        total_score = 0

        for idx, name in enumerate(self.name_list, 1):

            sum_of_alphabet = 0

            for letter in name.lower():
                sum_of_alphabet += self.alpha_dict[letter]

            score = idx * sum_of_alphabet
            total_score += score

        return total_score

def main():
    euler_22 = names_scores()
    euler_22.read_file()
    print(euler_22())

if __name__ == "__main__":
    main()
