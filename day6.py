from utils import get_input

input = get_input(6, False)

rows = len(input)
cols = len(input[0])

grid = {}
for r in range(rows):
    for c in range(cols):
        grid[(r,c)] = input[r][c]

# PART 1

start_location = (0,0)

# Identify the starting position
for r in range(rows):
    for c in range(cols):
        if grid[(r,c)] == "^":
            start_location = (r,c)
            break

# Initially pointing up
dir = (-1,0)

next_dir = {
    (-1,0): (0,1),
    (0,1): (1,0),
    (1,0): (0,-1),
    (0,-1): (-1,0)
}

part1 = 0

location = start_location

while True:
    if grid[location] != "X":
        part1 += 1
        grid[location] = "X"
    
    # Get the next spot
    next_location = tuple(map(sum, zip(location, dir)))
    next_spot = grid.get(next_location, "")

    # Check if next spot is out of bounds -> finish
    if next_spot == "":
        break

    # Check if next spot is an obstruction -> rotate
    if next_spot == "#":
        dir = next_dir[dir]
        continue

    # Otherwise move forward
    location = next_location

# PART 2 (yes this is a horrible brute force solution)

grid = {}
for r in range(rows):
    for c in range(cols):
        grid[(r,c)] = input[r][c]

part2 = 0

for r in range(rows):
    for c in range(cols):
        if grid[(r,c)] == ".":
            # Potential spot for an obstruction
            new_grid = grid.copy()
            new_grid[(r,c)] = "#"
            path = {}
            location = start_location
            dir = (-1,0)
            while True:
                if new_grid[location] != "X":
                    path[location] = {dir}
                    new_grid[location] = "X"
                else:
                    # See if we are in a loop (i.e. same location and direction as previously)
                    if dir in path[location]:
                        part2 += 1
                        break
                    path[location].add(dir)

                # Get the next spot
                next_location = tuple(map(sum, zip(location, dir)))
                next_spot = new_grid.get(next_location, "")

                # Check if next spot is out of bounds -> finish
                if next_spot == "":
                    break

                # Check if next spot is an obstruction -> rotate
                if next_spot == "#":
                    dir = next_dir[dir]
                    continue

                # Otherwise move forward
                location = next_location

print("Part 1:", part1)
print("Part 2:", part2)