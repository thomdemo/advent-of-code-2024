lines = [line.strip("\n") for line in open("inputs/day12.txt")]
lines = [list(line) for line in lines]

n = len(lines)


def get_neighbors(x, i, j):
    """Touching horizontally or vertically. No outside of garden."""
    n = len(x)
    neighbors = []
    for ii, jj in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
        if 0 <= ii < n and 0 <= jj < n:
            neighbors.append((ii, jj))
    return neighbors


# Global visited plants
visited = set()

groups = {}

group_id = 0

# Find adjacent regions
while len(visited) < n**2:

    for i in range(n):
        for j in range(n):
            if (i, j) not in visited:

                letter = lines[i][j]

                group = set()

                todo_stack = [(i, j)]

                while len(todo_stack) != 0:
                    i, j = todo_stack.pop()
                    group.add((i, j))
                    visited.add((i, j))
                    neighbors = get_neighbors(lines, i, j)
                    for ii, jj in neighbors:
                        if lines[i][j] == lines[ii][jj]:
                            if (ii, jj) not in group:
                                todo_stack.append((ii, jj))

                groups[group_id] = group
                group_id += 1


def nb_edges(lines, i, j):
    """Number of edges contributing to a perimeter."""
    letter = lines[i][j]
    n = len(lines)
    edges = 0
    for nei_i, nei_j in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
        if 0 <= nei_i < n and 0 <= nei_j < n:
            if lines[nei_i][nei_j] != letter:
                edges += 1
        else:
            # Outside of garden
            edges += 1
    return edges


# Compute price
price = 0
areas = []
for plants in groups.values():
    perimeter = sum(nb_edges(lines, i, j) for (i, j) in plants)
    area = len(plants)
    areas.append(area)
    price += area * perimeter
print(price)
