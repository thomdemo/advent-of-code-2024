import numpy as np


lines = [list(line.strip("\n")) for line in open("inputs/day04.txt")]


def count_xmas(x):
    s = 0
    for i in range(1, len(x) - 1):
        for j in range(1, len(x) -1):
            s += (x[i][j] == "A" and x[i-1][j-1] == "M"
                                 and x[i+1][j-1] == "M"
                                 and x[i-1][j+1] == "S"
                                 and x[i+1][j+1] == "S")
    return s


rotate = lambda x: np.vstack([arr[::-1] for arr in np.array(x).T])


s = count_xmas(lines)
for _ in range(3):
    lines = rotate(lines)
    s += count_xmas(lines)

print(s)
