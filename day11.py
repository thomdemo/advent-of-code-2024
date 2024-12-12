lines = [line.strip("\n") for line in open("inputs/day11.txt")]
line = [line.split() for line in lines][0]


def blink(line):
    new_line = []
    for stone in line:
        if stone == "0":
            new_line.append("1")
        elif len(stone) % 2 == 0:
            new_line.append(str(int(stone[:len(stone) // 2])))
            new_line.append(str(int(stone[len(stone) // 2:])))
        else:
            new_line.append(str(int(stone) * 2024))
    return new_line

for _ in range(25):
    line = blink(line)

print(len(line))
