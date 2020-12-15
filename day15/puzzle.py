import argparse
from collections import defaultdict

def memory_game(array, target_sum=30000000):
    tracker = {}
    for idx, element in enumerate(array):
        tracker[element] = idx

    prev_number = array[-1]
    for idx in range(len(array), target_sum):
        if prev_number in tracker:
            new_prev_number = (idx-1)-tracker[prev_number]
            tracker[prev_number] = idx-1
            prev_number = new_prev_number
        else:
            tracker[prev_number] = idx - 1 
            prev_number = 0
    
    return prev_number


def main():
    test_input_1 = [11,18,0,20,1,7,16]
    value = memory_game(test_input_1)
    print(value)

main()
