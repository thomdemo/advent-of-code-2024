from itertools import groupby

import numpy as np


# Parse input

# Line by line
lines = [line.strip("\n") for line in open("inputs/day13.txt")]

# Split systems
systems = [list(group) for k, group in
           groupby(lines, key=lambda x: x == "") if not k]

# Get values
systems_values = []
for s in systems:
    values = []
    for line_idx, line in enumerate(s):
        sep = "+" if line_idx < 2 else "="
        values.extend([int(txt.split(sep)[1]) for txt in line.split(",")])
    systems_values.append(values)

# Solve systems
sum_sol = 0
for system in systems_values:
    button_a_x, button_a_y, button_b_x, button_b_y, x, y = system
    # Part 2 variation: higher prize
    x += 10000000000000
    y += 10000000000000
    # Linear system: Ax = b
    A = np.array([[button_a_x, button_b_x], [button_a_y, button_b_y]],
                 dtype=np.float64)  # I think this is important
    b = np.array([x, y], dtype=np.float64)
    det = A[0][0] * A[1][1] - A[1][0] * A[0][1]
    if det != 0:
        # Matrix is invertible
        A_inverse = np.array([[A[1][1], -A[0][1]], [-A[1][0], A[0][0]]],
                             dtype=np.float64) / det
        sol = np.matmul(A_inverse, b)
        if sol[0] >= 0 and sol[1] >= 0:  # Not sure this is needed
            tol = 1e-3
            if (abs(sol[0] - round(sol[0])) < tol and
                abs(sol[1] - round(sol[1])) < tol):
                # Apply custom costs for button A and B
                sum_sol += round(sol[0]) * 3 + round(sol[1])

print(sum_sol)
