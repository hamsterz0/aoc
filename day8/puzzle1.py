import argparse

class Instruction:
    def __init__(self, name, value):
        self.name = name
        self.value = value

def get_instructions(filename):
    instructions = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip('\n').split(' ')
            instruction = Instruction(line[0], int(line[1]))
            instructions.append(instruction)
    return instructions

def calc_acc(instructions):
    visited = set()
    acc = 0
    current_idx = 0
    if not instructions:
        return 0
    instruction = instructions[current_idx]
    while current_idx not in visited:
        visited.add(current_idx)
        if instruction.name == 'acc':
            acc += instruction.value
            current_idx += 1
        elif instruction.name == 'jmp':
            current_idx += instruction.value
        else:
            current_idx += 1
        if current_idx >= len(instructions):
            break

        instruction = instructions[current_idx]

    return acc



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', required=True)
    args = parser.parse_args()

    instructions = get_instructions(args.filename)
    value = calc_acc(instructions)
    print(value)

main()
