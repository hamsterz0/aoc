
class Password:
    def __init__(self):
        self.least = 0
        self.most = 0
        self.char = 'a'
        self.password = ''

    def read_line(self, line):
        length, char, self.password = line.split(' ')
        self.char = char[0]
        self.least = int(length.split('-')[0])
        self.most = int(length.split('-')[-1])

    def is_correct(self):
        count = 0
        for char in self.password:
            if char == self.char:
                count += 1
            if count > self.most:
                return 0
        if count < self.least:
            return 0
        return 1
        

def number_of_correct_passwords(input_file):
    count = 0
    with open(input_file, 'r') as f:
        for line in f:
            password = Password()
            password.read_line(line)
            count += password.is_correct()
    return count

def main():
    correct_passwords = 0
    input_file = 'input2.txt'
    correct_passwords = number_of_correct_passwords(input_file)
    print(correct_passwords)

if __name__ == '__main__':
    main()
