lines = [line.strip("\n") for line in open("inputs/day06.txt")]
n = len(lines)

# Find start
for idx, line in enumerate(lines):
    if "^" in line:
        start = (idx, line.index("^"))

# Start direction: up
start_dir = (-1, 0)

# Figure out next direction based on previous one
next_dirs = {(-1, 0): (0, 1),
             (0, 1): (1, 0),
             (1, 0): (0, -1),
             (0, -1): (-1, 0)}


def can_exit(lines):

    distance = 0

    i, j = start
    dir = start_dir
    # Keep visited locations and associated directions
    visited = {((i, j), dir)}

    # Move while inside
    while 0 < i < n - 1 and 0 < j < n - 1:
        # Next position
        next_i, next_j = i + dir[0], j + dir[1]
        if lines[next_i][next_j] == "#":
            # Turn right: update dir
            dir = next_dirs[dir]
        else:
            visited.add(((i, j), dir))
            i = next_i
            j = next_j
            if ((i, j), dir) in visited:
                # Starting looping again here
                return False, visited, None

        distance += 1

        # This is a hack
        # TODO: find a better way
        if distance > 1000000:
            return False, visited, None

    # if can exit, add last position before exiting
    return True, visited, (i, j)

_, visited, last_pos = can_exit(lines)
visited = {pos for pos, _ in visited if pos != start}
visited.add(last_pos)


# Try different obstruction options.
# Draw candidates from visited set.

candidates = visited

num_good_positions = 0
for candidate in candidates:

    # Work on a copy
    lines_obstructed = [list(line) for line in lines]
    # Place obstruction
    lines_obstructed[candidate[0]][candidate[1]] = "#"

    num_good_positions += not can_exit(lines_obstructed)[0]

print(num_good_positions)
