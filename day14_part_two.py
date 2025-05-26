# Parse input

# Line by line
lines = [line.strip("\n") for line in open("inputs/day14.txt")]

# Tile dimensions
nrows = 103
ncols = 101

# Initial positions and velocities
lines = [[txt.split("=")[1].split(",") for txt in line.split(" ")]
         for line in lines]

data = []
for line in lines:
    px, py = list(map(int, line[0]))
    vx, vy = list(map(int, line[1]))
    data.append((px, py, vx, vy))

positions = [[px, py] for px, py, _, _ in data]
# Look for cycles
positions_history = {tuple([tuple(pos) for pos in positions])}
picture_concat = ""
for i in range(100000):
    print(i)
    print(len(positions_history))
    for data_idx, (_, _, vx, vy) in enumerate(data):
        positions[data_idx][0] = (positions[data_idx][0] + vx) % ncols
        positions[data_idx][1] = (positions[data_idx][1] + vy) % nrows
    positions_history.add(tuple([tuple(pos) for pos in positions]))

    # Found after some visual inspection
    if i % 101 == 51 or i % 103 == 26:

        # Visual result
        picture = [[0 for _ in range(ncols)] for _ in range(nrows)]
        for px, py in positions:
            picture[py][px] += 1
        picture = "\n".join(["".join([elt if elt != "0" else "."
                                      for elt in list(map(str, line))])
                             for line in picture])
        picture_concat += str(i) + "\n" + picture + "\n"

# Write picture_concat to a text file - for inspection
with open("day14_output.txt", "w") as f:
    f.write(picture_concat)

# 1. cycle length = 10403
# 2. special patterns appear when i % 101 == 51 or i % 103 == 26
# 3. sieve using 2. then look for the Christmas tree
# 4. spend time looking for an Easter egg and realize that it's the tree
