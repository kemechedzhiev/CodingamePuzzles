# TODO You get a sudoku grid from a player and you have to check if it has been correctly filled.
#  A sudoku grid consists of 9×9 = 81 cells split in 9 sub-grids of 3×3 = 9 cells.
#  For the grid to be correct, each row must contain one occurrence of each digit (1 to 9),
#  each column must contain one occurrence of each digit (1 to 9) and each sub-grid
#  must contain one occurrence of each digit (1 to 9).
#  You shall answer true if the grid is correct or false if it is not.
# 1 2 3 4 5 6 7 8 9
# 4 5 6 7 8 9 1 2 3
# 7 8 9 1 2 3 4 5 6
# 9 1 2 3 4 5 6 7 8
# 3 4 5 6 7 8 9 1 2
# 6 7 8 9 1 2 3 4 5
# 8 9 1 2 3 4 5 6 7
# 2 3 4 5 6 7 8 9 1
# 5 6 7 8 9 1 2 3 4

def check_rows(grid):
    result = True
    for row in grid:
        a = set(row)
        result = result and (len(a) == 9 and sum(a) == 45)
    return result


def check_columns(grid):
    tr_grid = [list(elem) for elem in zip(*grid)]
    return check_rows(tr_grid)


def check_subgrid(grid):
    return True


def check(grid):
    return check_rows(grid) and check_columns(grid) and check_subgrid(grid)


if __name__ == '__main__':
    grid = list()
    for i in range(9):
        grid.append([int(i) for i in input().split()])
    print(str(check(grid)).lower())
