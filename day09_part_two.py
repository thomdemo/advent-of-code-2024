# Represents the layout of files and free space on the disk.
disk_map = [line.strip("\n") for line in open("inputs/day09.txt")][0]
disk_map = map(int, disk_map)

# Build representation
blocks = []
position = 0
for idx, size in enumerate(disk_map):
    # Skip odd indices, mark ID as -1
    id = -1 if idx % 2 != 0 else idx // 2
    # Record the block
    blocks.append((id, size, position))
    # Increment position
    position += size

# Move whole file blocks. Start from the highest ID.
idx = len(blocks) - 1
while idx > 0:

    if blocks[idx][0] != -1:  # Don't move free space

        # Candidate block to move
        id, size, position = blocks[idx]
        # Find if the block can be moved to the left
        free_spaces = [(block_idx, block) 
                       for block_idx, block in enumerate(blocks[:idx])
                       if block[0] == -1 and block[1] >= size]
        if free_spaces:
            free_space_idx, free_space = free_spaces[0]
            # Do the move
            del blocks[idx]
            free_space_id, free_space_size, free_space_position = free_space
            if free_space_size == size:
                blocks[free_space_idx] = (id, size, free_space_position)
            else:
                # Consider residual free space
                blocks = (blocks[:free_space_idx] +
                          [(id, size, free_space_position),
                           (-1,
                            free_space_size - size,
                            free_space_position + size)] +
                          blocks[free_space_idx+1:])
    idx -= 1

# File checksum
acc = 0
for id, size, pos in blocks:
    if id != -1:
        for extra_pos in range(size):
            acc += id * (pos + extra_pos)
print(acc)
