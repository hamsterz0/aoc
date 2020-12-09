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
    for idx, number in enumerate(numbers):
        if sum_exist(number, lookup, preamble):
            lookup.remove(preamble[0])
            lookup.add(number)
            del preamble[0]
            preamble.append(number)
        else:
            return number, idx
    return None, -1

def calculate_incremental_sum(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return number

def find_sum(numbers, stop_idx, target_sum):
    start = 0
    current_sum = 0
    for i in range(0, stop_idx):
        current_sum += numbers[i]
        while current_sum > target_sum and start < i:
            current_sum -= numbers[start]
            start += 1
        if current_sum == target_sum:
            return min(numbers[start:i+1]) + max(numbers[start:i+1])
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', required=True)
    parser.add_argument('-p', '--preamble', type=int, required=True)
    args = parser.parse_args()

    numbers = get_numbers(args.filename)
    preamble = numbers[:args.preamble]
    invalid_number, idx = find_non_valid(args.filename, preamble, numbers[args.preamble:])
    sum_value = find_sum(numbers, idx, invalid_number)
    print(sum_value)
    

main()
