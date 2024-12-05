from utils import get_input

input = get_input(2)

def valid(parts):
    valid = True
    for i in range(1, len(parts)):
        if abs(parts[i] - parts[i-1]) > 3:
            valid = False
            break
    if not valid:
        return False
    asc = True
    desc = True
    for i in range(1, len(parts)):
        if parts[i] >= parts[i-1]:
            desc = False
        if parts[i] <= parts[i-1]:
            asc = False
    return asc or desc

# PART 1

part1=0
for line in input:
    parts = [int(p) for p in line.split()]
    part1 += valid(parts)

# PART 2

part2 = 0
for line in input:
    parts = [int(p) for p in line.split()]
    if valid(parts):
        part2 += 1
        continue
    # Else invalid
    for i in range(len(parts)):
        new_parts = parts.copy()
        new_parts.pop(i)
        if valid(new_parts):
            part2 += 1
            break
    
print("Part 1:", part1)
print("Part 2:", part2)