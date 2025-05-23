lines = [line.strip("\n") for line in open("inputs/day12.txt")]
lines = [list(line) for line in lines]

# Square matrix size
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


def outside_edges(cells):
    edges = set()
    for i, j in cells:
        # All 4 sides of a cell
        cell_edges = [frozenset({(i, j), (i + 1, j)}),  # West
                      frozenset({(i + 1, j), (i + 1, j + 1)}),  # South
                      frozenset({(i + 1, j + 1), (i, j + 1)}),  # East
                      frozenset({(i, j + 1), (i, j)})]  # North
        # An edge that belongs to two cells is not outside
        for cell_edge in cell_edges:
            if cell_edge not in edges:
                edges.add(cell_edge)
            else:
                edges.remove(cell_edge)
    return edges


def group_adjacent_edges(edges_in):

    # Work on a copy
    edges = edges_in.copy()
    # First edge: take any
    edge = edges.pop()
    visited = [edge]
    # Choose any vertex to connect the next edge
    vertex = next(iter(edge))

    # Visit all adjacent edges
    while edges:
        adjacent_edges = [e for e in edges if vertex in e]
        if not adjacent_edges:
            break

        # Adding a constraint to fix my bug: no edge "crossing"
        if len(adjacent_edges) in {2, 3}:
            # Origin vertex
            old_vertex = next(iter(edge - {vertex}))
            keep = []
            for adjacent_edge in adjacent_edges:
                next_vertex = next(iter(adjacent_edge - {vertex}))
                # Crossing is defined by alignment of theses coordinates
                # while having multiple options for the next edge.
                if (old_vertex[0] == vertex[0] == next_vertex[0] or
                    old_vertex[1] == vertex[1] == next_vertex[1]):
                    # Remove candidate
                    keep.append(False)
                else:
                    keep.append(True)
            # Update candidates
            adjacent_edges = [e for e, k in zip(adjacent_edges, keep) if k]

        edge = adjacent_edges[0]

        visited.append(edge)
        # Remove visited edge
        edges.remove(edge)
        # Choose unused vertex
        vertex = [v for v in edge if v != vertex][0]
    return visited


def make_edge_groups(edges_in):
    # Several groups when sides are disjoints
    edges = edges_in.copy()
    groups = []
    while edges:
        group = group_adjacent_edges(edges)
        groups.append(group)
        edges = edges - set(group)
    return groups

def count_turns(edge_groups):

    num_turns = 0
    for group in edge_groups:
        # Don't forget last turn
        for edge, next_edge in zip(group, group[1:] + [group[0]]):
            # From coordinates to vector
            v1, v2 = edge
            x1 = (v1[0] - v2[0], v1[1] - v2[1])
            v1, v2 = next_edge
            x2 = (v1[0] - v2[0], v1[1] - v2[1])
            # Orthogonal consecutive edges means there is a turn
            if x1[0] * x2[0] + x1[1] * x2[1] == 0:
                num_turns += 1
    return num_turns


acc = 0
for cells in groups.values():
    edges = outside_edges(cells)
    edge_groups = make_edge_groups(edges)
    acc += len(cells) * count_turns(edge_groups)

print(acc)
