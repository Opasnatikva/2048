import random


BOARD_SIZE = 4


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


# Check if there are any empty spaces on the board
def board_full(list):
    for index in list:
        if index.count(" ") != 0:
            return False
    return True


# Check if there are any possible moves
def possible_moves(list):
    for element in list:
        for index in range(len(element)):
            if element[index] == element[index + 1]:
                return True
    return False

# Return a row of the board
def get_row(grid, index):
    return grid[index]


# Return a reversed order Line
def reverse(line):
    return line.reverse()


#



# Return a column of the board
def get_column(grid, index):
    column = []
    for row in grid:
        column.append(row[index])
    return column


# Determine whether the new value to be inserted into an empty space is 2 or 4
def input_value():
    a = random.choices([2, 4], weights = [9, 1])
    return str(a[0])


# Return empty cells from a line from the grid and sort them in a list
def empty_cells(list):
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
def glue_values(line, empty):
    for index in range(len(empty)):
        line.append(line.pop(empty[index]))


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


# Take Input and validate
def take_input():
    a = ""
    while a != "a" and a != "w" and a != "d" and a != "s":
        a = input("A for left. W for up. D for right. S for down.")
    return a


# Initiate Board
board = generate_board(BOARD_SIZE)


# Initial random number placements
insert_random(random_empty_square(all_the_empty_squares(board)), input_value())


insert_random(random_empty_square(all_the_empty_squares(board)), input_value())


print_grid(board)


# Begin turn sequence
while not board_full(board) and possible_moves(board):
    take_input()


    glue_values(board, get_empty_cells(all_the_empty_squares(board)))
    insert_random(random_empty_square(all_the_empty_squares(board)), input_value())

print("Game Over!")


def all to the left
    take input
    validate
    extract lines in order
    manipulate lines
    write lines back to grid
    insert new values in grid