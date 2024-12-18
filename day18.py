from utils import get_input
from queue import Queue

input = get_input(18)

# PART 1

grid = {complex(int(i.split(",")[0]), int(i.split(",")[1])): "#" for i in input[:1024]}

rows, cols = 71, 71

for r in range(rows):
    for c in range(cols):
        if complex(r,c) not in grid:
            grid[complex(r,c)] = "."

def get_min_steps(grid):
    min_steps = {}
    q = Queue()
    q.put((complex(0,0),0))
    while not q.empty():
        pos, steps = q.get()
        if pos not in min_steps:
            min_steps[pos] = steps
        else:
            if steps < min_steps[pos]:
                min_steps[pos] = steps
            else:
                continue
        if pos == complex(rows-1, cols-1):
            continue
        for change in [1, -1, 1j, -1j]:
            if grid.get(pos+change, "#") != "#":
                q.put((pos + change, steps + 1))
    
    return min_steps.get(complex(rows-1,cols-1), None)

print("Part 1:", get_min_steps(grid))

for coord in input[1024:]:
    grid[complex(int(coord.split(",")[0]), int(coord.split(",")[1]))] = "#"
    min_steps = get_min_steps(grid)
    if min_steps is None:
        print("Part 2:", coord)
        break