line = "".join([line.strip("\n") for line in open("inputs/day03.txt")])

s = 0
# Enable mul instructions
enable = True
# Start at the beginning, scan the whole input
idx = 0
while idx < len(line):
    if line[idx:idx+4] == "do()":
        enable = True
    if line[idx:idx+7] == "don't()":
        enable = False
    if enable:
        if line[idx:idx+4] == "mul(":
            # Find closing bracket
            idx_closing = line[idx+4:].index(")")
            # Test if inside expression is legit
            expr = line[idx+4:idx+4+idx_closing]
            if "," in expr:
                lr = expr.split(",")
                if len(lr) == 2:
                    l, r = lr
                    if l.isdigit() and r.isdigit():
                        s += int(l) * int(r)
    idx += 1

print(s)
