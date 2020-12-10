import argparse

def count_combinations(adapters):
    ways = []
    adapters.sort()
    adapters.append(max(adapters)+3)
    adapters.insert(0, 0)
    for i in reversed(range(0, len(adapters))):
        adapter = adapters[i]
        way = sum([1 for j in range(i+1, i+4) if j < len(adapters) and adapter+3 >= adapters[j]])
        ways.append(way)
    current_max = 1
    for i in range(1, len(ways)):
        if ways[i] > 1:
            total = sum(ways[i-ways[i]:i])
            current_max = max(total, current_max)
        ways[i] = current_max
    return ways[-1]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', required=True)
    args = parser.parse_args()
    adapters = []

    with open(args.filename, 'r') as f:
        for line in f:
            line = line.strip('\n')
            adapters.append(int(line))


    count = count_combinations(adapters)
    print(count)


main()
