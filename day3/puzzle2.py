import sys

def read_lines(filepath):
    lines = list()
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip("\n")
            lines.append(line)
    return lines

def calculate_trees_hit(slopes, row_counter, col_counter):
    total_rows = len(slopes)
    total_hits = 0
    unique_gen = len(slopes[0])
    row, col = row_counter, col_counter
    while row < total_rows:
        current_slope = slopes[row]
        current_slope_pos = col % unique_gen
        if current_slope[current_slope_pos] == '#':
            total_hits += 1
        row += row_counter
        col += col_counter
    return total_hits

def main():
   filepath = sys.argv[1] 
   rows = [1, 1, 1, 1, 2]
   cols = [1, 3, 5, 7, 1]
   slopes = list()
   slopes = read_lines(filepath)
   trees_hit = 1
   for row, col in zip(rows, cols):
       trees_hit *= calculate_trees_hit(slopes, row, col)
   print(trees_hit)

main()
