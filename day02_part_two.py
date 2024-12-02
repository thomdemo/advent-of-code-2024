lines = [line.strip() for line in open("inputs/day02.txt")]

num_unsafe_reports = 0
unsafe_line_indices = []
for line_idx, line in enumerate(lines):
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
            # Save unsafe line index for later
            unsafe_line_indices.append(line_idx)
            break

recovered = set()
for line_idx in unsafe_line_indices:
    levels = list(map(int, lines[line_idx].split()))
    # Try removing each element
    for idx in range(len(levels)):
        levels_copy = levels[:]
        del levels_copy[idx]
        # See if it's safe
        is_safe = True  # presumed safe
        is_first_inscrease = levels_copy[1] > levels_copy[0]
        for idx in range(1, len(levels_copy)):
            # Measure diff
            diff = levels_copy[idx] - levels_copy[idx - 1]
            # Direction
            is_increase = diff > 0
            if not ((1 <= abs(diff) <= 3) and (is_increase == is_first_inscrease)):
                is_safe = False
        if is_safe:
            recovered.add(line_idx)

print(len(lines) - num_unsafe_reports + len(recovered))
