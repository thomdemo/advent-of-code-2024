topo_map = [line.strip("\n") for line in open("inputs/day10.txt")]
topo_map = [list(map(int, line)) for line in topo_map]

def get_neighbors(i, j, matrix):
    """Neighbors inside matrix and one step above value."""
    candidates = [(i - 1, j),
                  (i + 1, j),
                  (i, j - 1),
                  (i, j + 1)]
    candidates_inside = [candidate for candidate in candidates
                         if (0 <= candidate[0] < len(matrix)
                             and 0 <= candidate[1] < len(matrix))]
    return [(candidate[0],
             candidate[1],
             matrix[candidate[0]][candidate[1]])
             for candidate in candidates_inside
             if matrix[candidate[0]][candidate[1]] == matrix[i][j] + 1]

score_acc = 0
# Square topo map
n = len(topo_map)
for ii in range(n):
    for jj in range(n):
        if topo_map[ii][jj] == 0:  # Start of a trail
            # Initial neighbors
            neighbors = get_neighbors(ii, jj, topo_map)
            trailhead_ends = set()
            while neighbors:
                i, j, val = neighbors.pop()
                if val == 9:  # Reached the end of the trail
                    trailhead_ends.add((i, j))
                neighbors.extend(get_neighbors(i, j, topo_map))
            score_acc += len(trailhead_ends)
print(score_acc)
