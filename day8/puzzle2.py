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


def check_cycle_end(instruction, instructions, current_idx, visited):
    acc = 0
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
            return True, acc
        instruction = instructions[current_idx]
    return False, None


def calc_acc(instructions):
    visited = set()
    acc = 0
    current_idx = 0
    if not instructions:
        return 0
    instruction = instructions[current_idx]
    while current_idx not in visited:
        if instruction.name == 'acc':
            acc += instruction.value
            visited.add(current_idx)
            current_idx += 1
        elif instruction.name  == 'jmp':
            instruction.name = 'nop'
            temp_visited = visited.copy()
            cycle_end, remaining_acc = check_cycle_end(instruction, instructions, current_idx, temp_visited)
            if cycle_end:
                acc += remaining_acc
                return acc
            instruction.name = 'jmp'
            visited.add(current_idx)
            current_idx += instruction.value
        elif instruction.name == 'nop':
            instruction.name = 'jmp'
            temp_visited = visited.copy()
            cycle_end, remaining_acc = check_cycle_end(instruction, instructions, current_idx, temp_visited)
            if cycle_end:
                acc += remaining_acc
                return acc
            instruction.name = 'nop'
            visited.add(current_idx)
            current_idx += 1
        instruction = instructions[current_idx]
    return None



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', required=True)
    args = parser.parse_args()

    instructions = get_instructions(args.filename)
    value = calc_acc(instructions)
    print(value)

main()
