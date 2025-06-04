from itertools import groupby

# Parse input

# Line by line
lines = [line.strip("\n") for line in open("inputs/day15.txt")]

# Split map and instruction moves
line_groups = [list(group) for k, group in
               groupby(lines, key=lambda x: x == "") if not k]

old_lines = [list(line) for line in line_groups[0]]
# Duplicate everything except robot
lines = []
for line in old_lines:
    new_line = []
    for char in line:
        chars = {"@": ["@", "."],
                 ".": [".", "."],
                 "#": ["#", "#"],
                 "O": ["[", "]"]}[char]
        new_line.extend(chars)
    lines.append(new_line)

# Box dimensions
nrows = len(lines)
ncols = len(lines[0])

# Instruction moves
moves = "".join(line_groups[1])

# Find robot starting position
row = ["@" in line for line in lines].index(True)
col = lines[row].index("@")

directions = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

for move in moves:
    dir = directions[move]
    next_cell = (row + dir[0], col + dir[1])
    if lines[next_cell[0]][next_cell[1]] in {"[", "]"}:
        # Figure out all the dependent objects to move
        # and whether they can all move or not

        # Stack (row idx, col idx, value)
        to_move = [next_cell + (lines[next_cell[0]][next_cell[1]],)]
        visited = set()
        # Empty and process stack
        while to_move:
            i, j, val = to_move.pop()
            visited.add((i, j, val))
            if val == "[":
                if (i, j + 1, "]") not in visited:
                    to_move.append((i, j + 1, "]"))
            else:
                if (i, j - 1, "[") not in visited:
                    to_move.append((i, j - 1, "["))
            if lines[i + dir[0]][j + dir[1]] in {"[", "]"}:
                to_move.append((i + dir[0],
                                j + dir[1],
                                lines[i + dir[0]][j + dir[1]]))

        can_move = True
        # Can *all* items in the visited set move?
        for i, j, val in visited:
            if lines[i + dir[0]][j + dir[1]] == "#":
                can_move = False
        if can_move:
            for i, j, val in visited:
                lines[i + dir[0]][j + dir[1]] = val

            new_free_spaces = ({(i, j) for i, j, _ in visited} -
                               {(i + dir[0], j + dir[1]) for i, j, _ in visited})
            for i, j in new_free_spaces:
                lines[i][j] = "."
            # Update robot position
            lines[row + dir[0]][col + dir[1]] = "@"
            lines[row][col] = "."
            row += dir[0]
            col += dir[1]

    if lines[next_cell[0]][next_cell[1]] == ".":
        # Move robot
        lines[row + dir[0]][col + dir[1]] = "@"
        lines[row][col] = "."
        # Update robot position
        row += dir[0]
        col += dir[1]

# Count sum
acc = 0
for row_idx, line in enumerate(lines):
    for col_idx, val in enumerate(line):
        if val == "[":
            acc += 100 * row_idx + col_idx
print(acc)
