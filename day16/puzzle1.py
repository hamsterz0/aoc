import argparse
from collections import namedtuple


def read_line(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip('\n')


def process_information(filename):
    my_ticket = list()
    nearby_tickets = list()
    ranges = list()
    empty_line_counter = 0
    Range = namedtuple('Range', ['low', 'high'])

    for line in read_line(filename):
        if not line:
            empty_line_counter += 1
            continue
        # If no empty lines so far, then this is for the ranges. 
        if empty_line_counter == 0:
            first, second = line.split(': ')[-1].split(' or ')
            first, second = first.split('-'), second.split('-')
            first_range = Range(int(first[0]), int(first[1]))
            second_range = Range(int(second[0]), int(second[1]))
            ranges.append(first_range)
            ranges.append(second_range)
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
    for r in ranges:
        if r.low <= value <= r.high:
            return True
    return False


def find_faulty_numbers(ranges, nearby_tickets):
    fault_list = list()
    for ticket in nearby_tickets:
        for value in ticket:
            if not in_some_range(value, ranges):
                fault_list.append(value)
                break
    return fault_list

            
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', required=True)
    args = parser.parse_args()

    ranges, my_ticket, nearby_tickets = process_information(args.filename)
    fault_numbers = find_faulty_numbers(ranges, nearby_tickets)
    print(sum(fault_numbers))

main()
