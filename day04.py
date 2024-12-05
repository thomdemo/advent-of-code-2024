import numpy as np


lines = [list(line.strip("\n")) for line in open("inputs/day04.txt")]


def straight(x):
    num_occurs = 0
    for li in x:
        num_occurs += "".join(li).count("XMAS")
        num_occurs += "".join(li)[::-1].count("XMAS")  # opposite direction
    return num_occurs


def diag(x):

    num_occurs = 0

    n = len(x)  # square

    # Figure out starters: "L" corner = bottom left
    starts = [(i, 0) for i in range(n)] + [(n-1, j) for j in range(1, n)]

    # Sizes of diag lines
    diag_sizes = list(range(n)) + list(range(n))[:-1][::-1]

    # Direction: NE
    for (i, j), size in zip(starts, diag_sizes):
        li = []
        for ii, jj in zip(range(i, i-size-1, -1), range(j, j+size+1)):
            li.append((x[ii][jj]))

        num_occurs += "".join(li).count("XMAS")
        num_occurs += "".join(li)[::-1].count("XMAS")  # opposite direction

    return num_occurs


num_occurs_global = 0
num_occurs_global += diag(lines)
num_occurs_global += straight(lines)

# Rotate 90 deg clockwise.
lines = np.vstack([arr[::-1] for arr in np.array(lines).T])
num_occurs_global += straight(lines)
num_occurs_global += diag(lines)

print(num_occurs_global)
