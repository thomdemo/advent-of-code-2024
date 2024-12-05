lines = [line.strip("\n") for line in open("inputs/day05.txt")]

# Split rules and upudates
rules = [tuple(map(int, item.split("|"))) for item in lines[:lines.index("")]]
updates = [list(map(int, seq.split(","))) for seq in lines[lines.index("")+1:]]


def is_ordered(update):

    for idx, page in enumerate(update):

        l_neighbors = update[:idx]
        r_neighbors = update[idx+1:]

        # Scan over all rules
        # left
        for l_rule, r_rule in rules:
            if page == l_rule:
                if r_rule in l_neighbors:
                    return False
        # right
            if page == r_rule:
                if l_rule in r_neighbors:
                    return False
    return True


def find_swap_indices(update):
    for page_idx, page in enumerate(update):
        for neighbor_idx in range(page_idx+1, len(update)):
            for l, r in rules:
                if page == r and update[neighbor_idx] == l:
                    return page_idx, neighbor_idx

# Swap until sorted

from collections import defaultdict

num_swaps = defaultdict(int)

for update_idx in range(len(updates)):
    while not is_ordered(updates[update_idx]):
        i1, i2 = find_swap_indices(updates[update_idx])
        updates[update_idx][i1], updates[update_idx][i2] = updates[update_idx][i2], updates[update_idx][i1]
        num_swaps[update_idx] += 1

print(sum(update[len(update) // 2]
          for idx, update in enumerate(updates) if num_swaps[idx] != 0))
