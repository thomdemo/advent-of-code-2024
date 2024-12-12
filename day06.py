lines = [line.strip("\n") for line in open("inputs/day06.txt")]
n = len(lines)


# Find start
for idx, line in enumerate(lines):
    if "^" in line:
        start = (idx, line.index("^"))

# Figure out next direction based on previous one
next_dirs = {(-1, 0): (0, 1),
             (0, 1): (1, 0),
             (1, 0): (0, -1),
             (0, -1): (-1, 0)}

visited = set()
i, j = start
# Start direction: up
dir = (-1, 0)
# Move while inside
while 0 < i < n - 1 and 0 < j < n - 1:
    # Next position
    next_i, next_j = i + dir[0], j + dir[1]
    if lines[next_i][next_j] == "#":
        # Turn right: update dir
        dir = next_dirs[dir]
    else:
        visited.add((i, j))
        i = next_i
        j = next_j

print(len(visited) + 1)
