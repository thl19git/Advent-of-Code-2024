from utils import get_input

input = get_input(12)

rows = len(input)
cols = len(input[0])

grid = {}
for r in range(rows):
    for c in range(cols):
        grid[(r,c)] = ord(input[r][c])

# PARTS 1 AND 2

def get_area_perim(r, c, num, all_sides):
    n = grid.get((r,c), -1)
    if n != num:
        return 0
    grid[(r,c)] = num+32
    area = 1
    for new_r, new_c, side in [(r+1,c,"B"),(r-1,c,"T"),(r,c-1,"L"),(r,c+1,"R")]:
        area += get_area_perim(new_r, new_c, num, all_sides)
        if grid.get((new_r,new_c), -1) not in [num, num+32]:
            all_sides.append((r,c,side))
    return area

def reduce_sides(sides):
    bottom = [(side[0],side[1]) for side in sides if side[2]=="B"]
    top = [(side[0],side[1]) for side in sides if side[2]=="T"]
    left = [(side[1],side[0]) for side in sides if side[2]=="L"]
    right = [(side[1],side[0]) for side in sides if side[2]=="R"]

    num_sides = 4 # Minimum for a region
    for sides in [bottom, top, left, right]:
        sides.sort()
        for i in range(1, len(sides)):
            if sides[i][0] != sides[i-1][0]:
                num_sides += 1
            elif sides[i][1] != sides[i-1][1] + 1:
                num_sides += 1
    return num_sides

part1, part2 = 0, 0
for r in range(rows):
    for c in range(cols):
        if 90 >= grid[(r,c)] >= 65:
            sides = []
            area = get_area_perim(r, c, grid[(r,c)], sides)
            part1 += area * len(sides)
            actual_sides = reduce_sides(sides)
            part2 += area * actual_sides

print("Part 1:", part1)
print("Part 2:", part2)