import numpy as np


lines = [line.strip("\n") for line in open("inputs/day11.txt")]
line = [line.split() for line in lines][0]

def blink(line):
    new_line = []
    for stone in line:
        if stone == "0":
            new_line.append("1")
        elif len(stone) % 2 == 0:
            n = len(stone) // 2
            new_line.extend([stone[:n], str(int(stone[n:]))])
        else:
            new_line.append(str(int(stone) * 2024))
    return new_line

# First pass
for _ in range(42):
    print(_)
    line = blink(line)
    print(len(line))

values, counts = np.unique(line, return_counts=True)

del line

# Second pass
s = 0
for stone_idx, (stone, stone_count) in enumerate(zip(values, counts)):
    tmp = [stone]
    for _ in range(33):
        tmp = blink(tmp)
    s += len(tmp) * stone_count

print(s)
