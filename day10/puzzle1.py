import argparse

def calculate_chain(adapters):
    stack = list()
    adapters.sort()
    differences = [adapters[i]-adapters[i-1] for i in range(1, len(adapters))]
    return differences.count(1)+1, differences.count(3)+1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', required=True)
    args = parser.parse_args()
    adapters = []

    with open(args.filename, 'r') as f:
        for line in f:
            line = line.strip('\n')
            adapters.append(int(line))

    ones, threes = calculate_chain(adapters)
    print(ones, threes, ones*threes)

main()
