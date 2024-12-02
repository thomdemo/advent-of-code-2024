lines = [line.strip() for line in open("inputs/day01.txt")]

# Split lists, sort them.
left = sorted([int(line.split()[0].strip()) for line in lines])
right = sorted([int(line.split()[1].strip()) for line in lines])

print(sum([abs(l - r) for l, r in zip(left, right)]))

