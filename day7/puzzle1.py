import argparse


class BigBag:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return "color: {}".format(self.color)

class SmallBag:
    def __init__(self):
        self.color = None
        self.quant = None

    def parse_information(self, bag_string):
        bag_string = bag_string.split(' ')
        if 'no' in bag_string:
            self.quant = 0
        else:
            self.quant = bag_string[0]
        self.color = ' '.join(bag_string[1:-1])
    
    def __str__(self):
        return 'color: {} quant {}'.format(self.color, self.quant)


def read_line(filename):
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip("\n")
            line = line[:-1].split(' ')
            contain_idx = line.index('contain')
            big_bag = BigBag(' '.join(line[:contain_idx-1]))
            smaller_bags = ' '.join(line[contain_idx+1:]).split(', ')
            sbag_list = list()
            for bag in smaller_bags:
                small_bag = SmallBag()
                small_bag.parse_information(bag)
                sbag_list.append(small_bag)
            yield [big_bag, sbag_list]

                

def compute_bag_numbers(target_color, filename):
    mapping = dict()
    for big_bag, sbag_list in read_line(filename):
        for small_bag in sbag_list:
            if small_bag.color not in mapping:
                mapping[small_bag.color] = []
            mapping[small_bag.color].append(big_bag.color)
    
    stack = mapping[target_color]
    color_set = set(stack)
    while stack:
        new_color = stack.pop()
        if new_color not in mapping:
            continue
        color_set.update(mapping[new_color])
        if mapping[new_color]:
            stack.extend(mapping[new_color])
    return len(color_set)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', required=True)
    args = parser.parse_args()
    count = compute_bag_numbers('shiny gold', args.filename)
    print(count)


main()
