import argparse

def get_line(filename):
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip('\n')
            yield line

def calculate_yes_count(filename):
    count = 0
    yes_questions = set()
    for line in get_line(filename):
        if not line:
            count += len(yes_questions)
            yes_questions = set()
        else:
            yes_questions.update(line)
    # for the last batch
    count += len(yes_questions)
    return count

def main():
   parser = argparse.ArgumentParser()
   parser.add_argument('-f', '--filename', required=True)
   args = parser.parse_args()
   count = calculate_yes_count(args.filename)
   print(count)

main()
