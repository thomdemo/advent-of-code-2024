line = [line.strip("\n") for line in open("inputs/day09.txt")][0]

li = []
id = 0
for idx, digit in enumerate(line):
    if idx % 2 == 0:
        li.extend([str(id)]*int(digit))
        id += 1
    else:
        li.extend(["."]*int(digit))

# Moving file blocks
while "." in "".join(li).strip("."):
    value = li.pop()
    idx = li.index(".")
    li[idx] = value

li = [item for item in li if item != "."]

# Update file system checksum
print(sum(idx * int(value) for idx, value in enumerate(li)))
