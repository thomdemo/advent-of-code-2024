lines = [line.strip() for line in open("inputs/day01.txt")]

# Split lists.
left = [int(line.split()[0].strip()) for line in lines]
right = [int(line.split()[1].strip()) for line in lines]

# Value counts for right list.
counts = {val: right.count(val) for val in right}

print(sum([counts[l] * l for l in left if l in right]))
