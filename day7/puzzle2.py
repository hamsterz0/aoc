import argparse


class BigBag:
    def __init__(self, color):
        self.color = color
        self.small_bags = []
    
    def add_small_bag(self, small_bag):
        self.small_bags.append(small_bag)

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
            return
        self.quant = int(bag_string[0])
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
            for bag in smaller_bags:
                small_bag = SmallBag()
                small_bag.parse_information(bag)
                big_bag.add_small_bag(small_bag)
                yield big_bag
                

def recurse(bag_list, mapping):
    if not bag_list:
        return 0

    count = 0
    for bag in bag_list:
        count += bag.quant
        if not bag.color or bag.color not in mapping:
            return 0
        count += bag.quant*recurse(mapping[bag.color], mapping)
    return count


def compute_bag_numbers(target_color, filename):
    mapping = dict()
    for big_bag in read_line(filename):
        mapping[big_bag.color] = big_bag.small_bags

    if target_color not in mapping:
        return 1
    
    return recurse(mapping[target_color], mapping)
    


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', required=True)
    args = parser.parse_args()
    count = compute_bag_numbers('shiny gold', args.filename)
    print(count)


main()
