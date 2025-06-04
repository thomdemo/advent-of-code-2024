from itertools import groupby

# Parse input

# Line by line
lines = [line.strip("\n") for line in open("inputs/day15.txt")]

# Split map and instruction moves
line_groups = [list(group) for k, group in
               groupby(lines, key=lambda x: x == "") if not k]

lines = [list(line) for line in line_groups[0]]
n = len(lines)  # Box size
moves = "".join(line_groups[1])

# Find robot starting position
row = ["@" in line for line in lines].index(True)
col = lines[row].index("@")

directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def get_path(dir: str, row: int, col: int, n: int):
    if dir == "^":
        path = [(row - (i + 1), col) for i in range(row)]
    elif dir == "v":
        path = [(row + i + 1, col) for i in range(n - row - 1)]
    elif dir == ">":
        path = [(row, col + i + 1) for i in range(n - col - 1)]
    elif dir == "<":
        path = [(row, col - (i + 1)) for i in range(col)]
    else:
        raise ValueError(f"Invalid direction: {dir}")
    return path


for move in moves:
    # What is on the robot's way
    path = get_path(move, row, col, n)
    dir = directions[move]

    objects_on_path = [lines[i][j] for i, j in path]  # Including edge wall

    # Either edge wall or early wall on the way
    first_wall_idx = objects_on_path.index("#")
    movable_objects = [path[:first_wall_idx], objects_on_path[:first_wall_idx]]

    if "." in movable_objects[1]:  # Do something
        first_free_idx = movable_objects[1].index(".")  # Useless?
        to_move = [movable_objects[0][:first_free_idx],
                   movable_objects[1][:first_free_idx]]
        if not to_move[0] or "O" not in to_move[1]:
            # Just move the robot
            (lines[row][col],
             lines[row + dir[0]][col + dir[1]]) = (lines[row + dir[0]][col + dir[1]],
                                                   lines[row][col])
            # Update robot coordinates
            row += dir[0]
            col += dir[1]
        else:  # Bunch of Os to move 
            for (i, j), val in zip(to_move[0] + [(row, col)], to_move[1] + ["@"]):
                lines[i + dir[0]][j + dir[1]] = val
            lines[row][col] = "."  # Fill robot's value
            # Update robot coordinates
            row += dir[0]
            col += dir[1]

# Compute answer
acc = 0
for row_idx, line in enumerate(lines):
    for col_idx, val in enumerate(line):
        if val == "O":
            acc += 100 * row_idx + col_idx
print(acc)
