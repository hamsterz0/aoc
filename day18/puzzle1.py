import argparse
from collections import namedtuple

State = namedtuple('State', ['digit', 'op'])

def get_line(filename):
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip('\n').replace('(', '( ').replace(')', ' )').split(' ')
            yield line


def collapse_stack(stack):
    top = stack.pop()
    current = 0
    while top.digit:
        current = current + top.digit if top.op == '+' or not top.op else current * top.digit
        if stack:
            top = stack.pop()
        else:
            break
    stack.append(State(current, top.op))

                
def process_math_problem(line):
    stack = list()
    for char in reversed(line):
        if char.isdigit():
            stack.append(State(int(char), None))
        elif char == ')':
            stack.append(State(None, None))
        elif char in '+*':
            top = stack.pop()
            new_top = State(top.digit, char)
            stack.append(new_top)
        else:
            collapse_stack(stack)

    collapse_stack(stack)
    return stack[-1].digit


def calculate_sum(filename):
    current_sum = 0
    for line in get_line(filename):
        result = process_math_problem(line)
        current_sum += result
    return current_sum

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', required=True)
    args = parser.parse_args()

    result_sum = calculate_sum(args.filename)
    print(result_sum)


main()
