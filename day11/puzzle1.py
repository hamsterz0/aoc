import argparse

def read_data(filename: str) -> list:
    matrix = list()
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip('\n')
            row = [char for char in line]
            matrix.append(row)
    return matrix


def can_sit(i: int, j: int, matrix: list) -> list:
    nr, nc = len(matrix), len(matrix[0])
    for r in range(-1, 2):
        for c in range(-1, 2):
            if r == 0 and c == 0:
                continue
            if 0 <= i+r < nr and 0 <= j+c < nc:
                if matrix[i+r][j+c] not in '.L%':
                    return False
    return True

def can_move(i: int, j: int, matrix: list) -> list:
    nr, nc = len(matrix), len(matrix[0])
    counter = 0
    for r in range(-1, 2):
        for c in range(-1, 2):
            if r == 0 and c == 0:
                continue
            if 0 <= i+r < nr and 0 <= j+c < nc:
                if matrix[i+r][j+c] in '#@':
                    counter += 1
    return True if counter > 3 else False


def final_stablized_matrix(matrix):
    if not matrix or not matrix[0]:
        return 0

    nr, nc = len(matrix), len(matrix[0])            # num rows, num cols
    while True:
        for i in range(0, nr):
            for j in range(0, nc):
                if matrix[i][j] == '.':             # if . then skip
                    continue
                if matrix[i][j] == 'L':             
                    if can_sit(i, j, matrix):
                        matrix[i][j] = '%'          # % is the placeholder for L->#
                if matrix[i][j] == '#':
                    if can_move(i, j, matrix):
                        matrix[i][j] = '@'          # @ is the placeholder for #->L

        was_change = False
        for i in range(0, nr):
            for j in range(0, nc):
                if matrix[i][j] in '@%':
                    matrix[i][j] = 'L' if matrix[i][j] == '@' else '#'
                    was_change = True

        if not was_change:
            break

    return matrix


def calc_occ_seats(matrix):
    count = 0
    for row in matrix:
        for value in row:
            if value == '#':
                count += 1
    return count

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', required=True)
    args = parser.parse_args()
    matrix = read_data(args.filename)
    matrix = final_stablized_matrix(matrix)
    occ_seats = calc_occ_seats(matrix)
    print(occ_seats)

main()
