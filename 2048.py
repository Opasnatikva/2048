import random


BOARD_SIZE = 4


# Dictionary of the possible inputs
directions = {'a' : 0, 'd' : 1, 'w' : 2,  's' : 3}


# Generate the board
def generate_board(size):
    daska = []
    for rows in range(size):
        daska.append([])
        for col in range(size):
            daska[rows].append(" ")
    return daska


# Display the game state
def print_grid(grid):
    for index in range(len(grid)):
        print(grid[index])


# Return a row of the board
def get_row(grid, index):
    return grid[index]


# Return a column of the board
def get_column(grid, index):
    column = []
    for row in grid:
        column.append(row[index])
    return column


# Return a reversed order Line
def reverse(line):
    return line.reverse()


# Check if there are any empty spaces on the board
def board_full(list):
    for index in list:
        if index.count(" ") != 0:
            return False
    return True


# Check if there are any possible moves
def moves_possible(grid):
    for element in grid:
        for index in range(len(element[1:-1])):
            if element[index] == element[index + 1]:
                return True
    return False

# Determine whether the new value to be inserted into an empty space is 2 or 4
def return_two_or_four():
    a = random.choices([2, 4], weights = [9, 1])
    return str(a[0])


# Return empty cells from a line from the grid and sort them in a list
def return_empty_cells(list):
    empty_fields = []
    for index in range(len(list)):
        empty_fields.append(list[index])
    return empty_fields

# Check if current values of two squares in a line are equal
def equal_values(line):
    for element in line:
        for index in range(len(line[1:])):
            if element != " " and element == line[index]:
                return True
            else:
                return False


# Return a list with the indexes of all empty spaces in a line of the grid
def get_empty_cells(line):
    empty_values = []
    for empty in range(len(line)):
        if line[empty] == " ":
            empty_values.append(empty)
    empty_values.reverse()
    return empty_values


# Move all empty spaces defined by "get_empty_cells" to the end of the line
def shift_values(line, indexes):
    for index in range(len(indexes)):
         line.append(line.pop(indexes[index]))
    return line

# Return a list of the indexes of all the empty elements in the grid
def all_the_empty_squares(list):
    a = ""
    list_of_empty = []
    for line_number in range(len(list)):
        line = list[line_number]
        for index in range(len(line)):
            if line[index] == " ":
                a = str(line_number) + " " + str(index)
                list_of_empty.append(a)
    return list_of_empty


# Draw random from all_the_empty_squares
def random_empty_square(list):
    return random.choice(list)

# Insert random into the grid
def insert_random(set, value):
    a = set.split()
    board[int(a[0])][int(a[1])] = value


def move_left(grid):
    for index in range(len(grid)):
        grid[index] = shift_values(get_row(grid, index), get_empty_cells(get_row(grid, index)))


# High score counter (the sum of all numbers)
def high_score(grid):
    score = 0
    for line in grid:
        for element in line:
            if element != " ":
                score += int(element)
    return score


# Take input, validate based on dictionary keys, and return the corresponding value from the dictionary
def move_direction(dictionary):
    while True:
        a = input("Type 'A' for left, 'W' for up, 'D' for right, or 'S' for down!")
        for key, value in dictionary.items():
            if a == key:
                return value
        print("Please enter a valid direction as stated below:")


# Initiate Board
board = generate_board(BOARD_SIZE)
print(high_score(board))
print_grid(board)

# Initial random number placements
insert_random(random_empty_square(all_the_empty_squares(board)), return_two_or_four())
insert_random(random_empty_square(all_the_empty_squares(board)), return_two_or_four())


# Begin turn sequence
while moves_possible(board) and not board_full(board):
    x = move_direction(directions)


    insert_random(random_empty_square(all_the_empty_squares(board)), return_two_or_four())
    print(high_score(board))
    print_grid(board)
print_grid(board)
print("Game Over!")
