# TODO Find the winning move for the O player on the following tic-tac-toe board.

def horizontal_win(game_field):
    horizontal_new_field = list()
    flag = False
    opponent_flag = False
    for row in game_field:
        count = 0
        for letter in row:
            if letter == 'O':
                count += 1
            elif letter == 'X':
                opponent_flag = True
                break
        if count == 2 and not opponent_flag:
            horizontal_new_field.append('OOO')
            flag = True
        else:
            horizontal_new_field.append(''.join(row))
    return flag, horizontal_new_field


def vertical_win(game_field):
    field_transposed = [list(line) for line in zip(*game_field)]
    flag, vertical_new_field = horizontal_win(field_transposed)
    if flag:
        vertical_new_field = [list(line) for line in zip(*vertical_new_field)]
    return flag, vertical_new_field


def diagonal_win(game_field):
    count = 0
    flag = False
    opponent_flag = False
    diagonal_new_field = list()
    for index in range(len(game_field)):
        value = game_field[index][index]
        if value == 'O':
            count += 1
        elif value == 'X':
            opponent_flag = True
            break
    if count == 2 and not opponent_flag:
        flag = True
        for i in range(len(game_field)):
            new_row = game_field[i]
            new_row[i] = 'O'
            diagonal_new_field.append(new_row)
    else:
        count = 0
        opponent_flag = False
        for index in range(len(game_field)):
            value = game_field[2 - index][index]
            if value == 'O':
                count += 1
            elif value == 'X':
                opponent_flag = True
                break
        if count == 2 and not opponent_flag:
            flag = True
            for index in range(len(game_field)):
                new_row = game_field[index]
                new_row[2-index] = 'O'
                diagonal_new_field.append(new_row)
    return flag, diagonal_new_field


if __name__ == '__main__':
    field = list()
    for i in range(3):
        line = input()
        field.append(list(line))
    win_flag, new_field = horizontal_win(field)
    if not win_flag:
        win_flag, new_field = vertical_win(field)
    if not win_flag:
        win_flag, new_field = diagonal_win(field)
    if win_flag:
        for row in new_field:
            print(''.join(row))
    else:
        print('false')
