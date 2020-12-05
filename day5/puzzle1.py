import argparse
import math

def get_line(filename):
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip('\n')
            yield line

def bsearch(locs, low, high):
    while locs:
        if locs[0].lower() in 'fl':
            high = (low + high) // 2
        elif locs[0].lower() in 'br':
            low = math.ceil((low + high)/2)
        locs = locs[1:]
    return min(low, high)

def compute_ids(filename):
    ids = []
    for line in get_line(filename):
        row = bsearch(line[:7], 0, 127)
        col = bsearch(line[7:], 0, 7)
        score = (row*8) + col
        ids.append(score)
    return ids


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', required=True);
    args = parser.parse_args()
    max_value = max(compute_ids(args.filename))
    print(max_value)

main()
