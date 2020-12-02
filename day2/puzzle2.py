
class Password:
    def __init__(self):
        self.first = 0
        self.second = 0
        self.char = 'a'
        self.password = ''

    def parse_line(self, line):
        loc, char, self.password = line.split(' ')
        self.char = char[0]
        self.first = int(loc.split('-')[0]) - 1
        self.second = int(loc.split('-')[-1]) - 1

    def is_correct(self):
        if self.first >= len(self.password) or self.second >= len(self.password):
            return 0
        combined = ''.join([self.password[self.first], self.password[self.second]])
        if self.char*2 == combined:
            return 0
        elif self.char not in combined:
            return 0
        return 1
        

def number_of_correct_passwords(input_file):
    count = 0
    with open(input_file, 'r') as f:
        for line in f:
            password = Password()
            password.parse_line(line)
            count += password.is_correct()
    return count

def main():
    correct_passwords = 0
    input_file = 'input2.txt'
    correct_passwords = number_of_correct_passwords(input_file)
    print(correct_passwords)

if __name__ == '__main__':
    main()
