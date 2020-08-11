import random
import copy

BOARD_SIZE = 4

adjacent_even_values = True


def generate_empty_board(board_size=BOARD_SIZE):
    board = []
    for row_index in range(board_size):
        row = []
        for col in range(board_size):
            row.append(" ")
        board.append(row)
    return board


def print_fancy_board(board):
    for row in board:
        print("|", ' | '.join(map(str, row)), "|")
        # print("{:^4}".format(str(row[0])))


def print_high_score(board):
    board_buff = []
    for row in board:
        for element in row:
            if element != " ":
                board_buff.append(element)
    print(sum(board_buff))


def get_empty_squares(board):
    a = []
    for row_index in range(len(board)):
        for square_index in range(len(board[row_index])):
            if board[row_index][square_index] == " ":
                a.append((row_index, square_index,))
    return a


def choose_empty_square(empty_list):
    if empty_list:
        return random.choice(empty_list)
    else:
        return False


def two_or_four():
    return random.choices((2, 4), (9, 1))[0]


# def get_column(board, index):
#     col_buffer = []
#     for row in board:
#         col_buffer.append(row[index])
#     return col_buffer


def switch_rows_columns(board):
    grid_buffer = []
    for index in range(len(board)):
        col_buffer = []
        for row in board:
            col_buffer.append(row[index])
        grid_buffer.append(col_buffer)
    return grid_buffer


def move_left(board):
    grid_buffer = []
    for row in board:
        line_buffer = []
        for index in range(len(row)):
            if row[index] != " ":
                line_buffer.append(row[index])
        for index in range(len(row) - len(line_buffer)):
            line_buffer.append(" ")
        grid_buffer.append(line_buffer)
    return grid_buffer


def flip_right(board):
    grid_buffer = []
    for row in board:
        row.reverse()
        grid_buffer.append(row)
    return grid_buffer


# dictionary = {"a": 0, "d": 1, "w": 2, "s": 3}


# def take_input(directions=dictionary):
#     while True:
#         a = input("Type 'a' for left, 'd' for right, 'w' for up, 's' for down.")
#         for key, value in directions.items():
#             if a == key:
#                 return value
#         print("Please enter a valid direction as stated below:")

def take_input():
    while True:
        a = input("Type 'a' for left, 'd' for right, 'w' for up, 's' for down.")
        if a in ["a", "d", "w", "s"]:
            return a
        print("Please enter a valid direction as stated below:")


def switch_case(board, player_input):
    """We doin it for da flex!"""
    if player_input == "a":
        return move_left(sum_adjacent_equal_numbers(move_left(board)))
    elif player_input == "d":
        return flip_right(move_left(sum_adjacent_equal_numbers(move_left(flip_right(board)))))
    elif player_input == "w":
        return switch_rows_columns(move_left(sum_adjacent_equal_numbers(move_left(switch_rows_columns(board)))))
    elif player_input == "s":
        return switch_rows_columns(
            flip_right(move_left(sum_adjacent_equal_numbers(move_left(flip_right(switch_rows_columns(board)))))))


# def adjacent_equal_numbers(board):
#     board_buffer = []
#     for row in board:
#         board_buffer.append(row)
#     board_comparison = []
#     while board_buffer != board_comparison:
#         board_comparison = []
#         for element in board_buffer:
#             board_comparison.append(element)
#         for row in board_buffer:
#             for index in range(len(row - 1)):
#                 if row[index] == row[index + 1]:
#                     row[index] *= 2
#                     row[index + 1] = " "
#     return board_buffer


def sum_adjacent_equal_numbers(board):
    board_buffer = []
    for row in board:
        board_buffer.append(row)
    for row in board_buffer:
        for index in range(len(row) - 1):
            if row[index] == row[index + 1] and row[index] != " ":
                row[index] *= 2
                row[index + 1] = " "
    return board_buffer


# def merge_list(something_something):
#     """Мърджваме един лист, просто"""
#     pass


# def iterate_merging(direction):
#     """Циклим всички листи в някаква посока"""
#     pass


def adjacent_pairs(board):
    for row in board:
        for index in range(len(row) - 1):
            if row[index] == row[index + 1] and row[index] != " ":
                return True
    return False


def random_empty_coors(board):
    return choose_empty_square(get_empty_squares(board))


def insert_random_number(board):
    x_and_y = random_empty_coors(board)
    if x_and_y:
        board[x_and_y[0]][x_and_y[1]] = two_or_four()


def board_full(board):
    for row in board:
        for element in row:
            if element == " ":
                return False
    return True


if __name__ == "__main__":
    grid = generate_empty_board()
    # for index in range(len(grid)):
    #     for col_index in range(len(grid)):
    #         grid[index][col_index] = (index + 3) * (col_index + 1)
    insert_random_number(grid)
    insert_random_number(grid)
    print_high_score(grid)
    print_fancy_board(grid)
    while not board_full(grid) or adjacent_even_values:
        old_grid = copy.deepcopy(grid)
        grid = switch_case(grid, take_input())
        if old_grid == grid and not board_full(grid):
            print_fancy_board(grid)
            continue
        x_and_y = random_empty_coors(grid)
        if x_and_y:
            grid[x_and_y[0]][x_and_y[1]] = two_or_four()
        print_high_score(grid)
        print_fancy_board(grid)
        if board_full(grid):
            adjacent_even_values = adjacent_pairs(grid)
            if not adjacent_even_values:
                adjacent_even_values = adjacent_pairs(switch_rows_columns(grid))
    print("Game over!")