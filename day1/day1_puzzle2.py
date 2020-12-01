
def read_input_file(filename):
    input_arr = []
    with open(filename, 'r') as f:
        for line in f:
            input_arr.append(int(line))
    return input_arr

def find_numbers(input_arr, target_sum):
    first_idx = 0
    last_idx = len(input_arr) - 1

    while first_idx < last_idx:
        ele1 = input_arr[first_idx]
        ele2 = input_arr[last_idx]
        ele_sum = ele1 + ele2

        if (ele_sum == target_sum):
            return [ele1, ele2]
        elif (ele_sum < target_sum):
            first_idx += 1
        else:
            last_idx -= 1

    return None


def find_three_numbers(input_arr, target_sum):
    input_arr.sort()
    for i in range(len(input_arr)-1):
        new_target = target_sum - input_arr[i]
        result = find_numbers(input_arr[i+1:], new_target)
        if result:
            return [input_arr[i], result[0], result[1]]
    return None


def main():
    filename = 'input2.txt'
    target_sum = 2020
    input_arr = read_input_file(filename)
    result = find_three_numbers(input_arr, target_sum)
    if result:
        return result[0] * result[1] * result[2]
    return None


if __name__ == '__main__':
    print(main())
