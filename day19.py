from utils import get_input
import functools

input = get_input(19)

towels = input[0].split(", ")
designs = input[2:]

@functools.cache
def ways(design):
    if not design:
        return 1
    count = 0
    for towel in towels:
        if design.find(towel) == 0:
            count += ways(design[len(towel):])
    return count

part1, part2 = 0, 0
for design in designs:
    w = ways(design)
    part1 += w > 0
    part2 += w

print("Part 1:", part1)
print("Part 2:", part2)