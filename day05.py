lines = [line.strip("\n") for line in open("inputs/day05.txt")]

# Split rules and upudates
rules = [tuple(map(int, item.split("|"))) for item in lines[:lines.index("")]]
updates = [list(map(int, seq.split(","))) for seq in lines[lines.index("")+1:]]

wrong_updates = set()
for update_idx, update in enumerate(updates):
    for idx, num in enumerate(update):
        for neighbor_idx in range(idx+1, len(update)):
            for rule in rules:
                l, r = rule
                if num == r and update[neighbor_idx] == l:
                    wrong_updates.add(update_idx)

# Not using an anti pattern again!
print(sum(update[len(update) // 2] for idx, update
          in enumerate(updates) if idx not in wrong_updates))
