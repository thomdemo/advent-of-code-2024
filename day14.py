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


top_left = top_right = bottom_left = bottom_right = 0
for px, py, vx, vy in data:
    for _ in range(100):
        px = (px + vx) % ncols
        py = (py + vy) % nrows
    # Quadrant count
    if px < ncols // 2:
        if py < nrows // 2:
            top_left += 1
        elif py > nrows // 2:
            bottom_left += 1
        else:
            pass  # middle
    elif px > ncols // 2:
        if py < nrows // 2:
            top_right += 1
        elif py > nrows // 2:
            bottom_right += 1
        else:
            pass  # middle

print(top_left * top_right * bottom_left * bottom_right)
