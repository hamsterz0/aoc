import argparse

def get_numbers(filename):
    numbers = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip('\n')
            numbers.append(int(line))
    return numbers

def sum_exist(target, lookup, preamble):
    for number in preamble:
        second_number = target-number
        if second_number in lookup and (second_number != number):
            return True
    return False


def find_non_valid(filename, preamble, numbers):
    lookup = set(preamble)
    for number in numbers:
        if sum_exist(number, lookup, preamble):
            lookup.remove(preamble[0])
            lookup.add(number)
            del preamble[0]
            preamble.append(number)
        else:
            return number
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', required=True)
    parser.add_argument('-p', '--preamble', type=int, required=True)
    args = parser.parse_args()

    numbers = get_numbers(args.filename)
    preamble = numbers[:args.preamble]
    not_valid_number = find_non_valid(args.filename, preamble, numbers[args.preamble:])
    print(not_valid_number)
    

main()
