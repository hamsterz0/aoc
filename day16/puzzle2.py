import argparse
from collections import namedtuple, defaultdict


def read_line(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip('\n')


def process_information(filename):
    my_ticket = list()
    nearby_tickets = list()
    ranges = defaultdict(list)
    empty_line_counter = 0
    Range = namedtuple('Range', ['low', 'high'])

    for line in read_line(filename):
        if not line:
            empty_line_counter += 1
            continue
        # If no empty lines so far, then this is for the ranges. 
        if empty_line_counter == 0:
            class_name = line.split(': ')[0]
            first, second = line.split(': ')[-1].split(' or ')
            first, second = first.split('-'), second.split('-')
            first_range = Range(int(first[0]), int(first[1]))
            second_range = Range(int(second[0]), int(second[1]))
            ranges[class_name].append(first_range)
            ranges[class_name].append(second_range)
        # If one empty line has been encountered, then it's my ticket time
        if empty_line_counter == 1:
            if not line[0].isdigit():
                continue
            my_ticket = [int(value) for value in line.split(',')]
        # If two empty lines, then it has be to be nearby ones. 
        if empty_line_counter == 2:
            if not line[0].isdigit():
                continue
            ticket = [int(value) for value in line.split(',')]
            nearby_tickets.append(ticket)
    return ranges, my_ticket, nearby_tickets


def in_some_range(value, ranges):
    class_set = set()
    found_range = False
    for class_name, range_values in ranges.items():
        for r in range_values:
            if r.low <= value <= r.high:
                class_set.add(class_name)
                found_range = True
    return (class_set, found_range)


def find_class_val_mapping(ranges, nearby_tickets):
    # for each index, create a empty set which will store all the sets of possible
    # classes that idx can have
    idx_class_mapping = defaultdict(set)
    for ticket in nearby_tickets:
        # list of class sets for each index
        class_sets = list()
        # A check to see if the current nearby_ticket is currently valid or not. 
        # initial observation is that it isn't
        invalid = False
        for idx, value in enumerate(ticket):
            class_set, found_range = in_some_range(value, ranges)
            if not found_range:
                invalid = True
                break
            else:
                class_sets.append(class_set)
        if not invalid:
            for idx, class_set in enumerate(class_sets):
                if not idx_class_mapping[idx]:
                    idx_class_mapping[idx] = class_set
                else:
                    idx_class_mapping[idx] = idx_class_mapping[idx].intersection(class_set)
    return idx_class_mapping


def normalize_mapping(mapping):
    mapping = sorted(mapping.items(), key=lambda x: len(x[1]))
    for i in range(0, len(mapping)-1):
        for j in range(i+1, len(mapping)):
            mapping[j] = (mapping[j][0], mapping[j][1] - mapping[i][1])

    return dict(mapping)


            
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', required=True)
    args = parser.parse_args()

    ranges, my_ticket, nearby_tickets = process_information(args.filename)
    idx_class_mapping = find_class_val_mapping(ranges, nearby_tickets)
    n_mapping = normalize_mapping(idx_class_mapping)

    prod_value = 1
    departure = {'departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time'}
    for idx, idx_set in n_mapping.items():
        if len(departure.intersection(idx_set)) > 0:
            prod_value *= my_ticket[idx]

    print(prod_value)


main()
