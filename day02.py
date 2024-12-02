lines = [line.strip("\n") for line in open("inputs/day02.txt")]

num_unsafe_reports = 0
for line in lines:
    levels = list(map(int, line.split()))
    # First direction
    is_first_inscrease = levels[1] > levels[0]
    for idx in range(1, len(levels)):
        # Measure diff
        diff = levels[idx] - levels[idx - 1]
        # Direction
        is_increase = diff > 0
        if not ((1 <= abs(diff) <= 3) and (is_increase == is_first_inscrease)):
            num_unsafe_reports += 1
            break

print(len(lines) - num_unsafe_reports)
