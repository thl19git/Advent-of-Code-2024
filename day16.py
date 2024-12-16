from utils import get_input
from queue import Queue

input = get_input(16, False)
grid = {}

start, end = None, None
for r, row in enumerate(input):
    for c, col in enumerate(row):
        if col == "S":
            start = complex(r, c)
        elif col == "E":
            end = complex(r, c)
        grid[complex(r,c)] = col

shortest_paths = {}

q = Queue()
q.put((start, 1j, 0, set()))

best_spots = set()
min_cost = 1000000000

while not q.empty():
    pos, dir, cost, visited = q.get()
    if pos in visited:
        # This path has taken us in a loop
        continue
    visited.add(pos)
    if pos not in shortest_paths:
        # Not visited this point before
        shortest_paths[pos] = {dir: cost}
    else:
        # Visited this point before, check if we did it in the best way
        if grid[pos] == "E":
            if cost < min_cost:
                best_spots = visited
                min_cost = cost
            elif cost == min_cost:
                best_spots = best_spots.union(visited)
        if dir not in shortest_paths[pos]:
            shortest_paths[pos][dir] = cost
        else:
            if shortest_paths[pos][dir] < cost:
                continue
            else:
                shortest_paths[pos][dir] = cost
    # See if we are at the end
    if grid[pos] == "E":
        continue
    # Find places to move to
    if grid[pos + dir] != "#":
        q.put((pos+dir, dir, cost+1, visited.copy()))
    if grid[pos + dir*complex(0,1)] != "#":
        q.put((pos + dir*complex(0,1), dir*complex(0,1), cost+1001, visited.copy()))
    if grid[pos + dir*complex(0,-1)] != "#":
        q.put((pos + dir*complex(0,-1), dir*complex(0,-1), cost+1001, visited.copy()))

print("Part 1:", min_cost)
print("Part 2:", len(best_spots))