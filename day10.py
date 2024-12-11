from utils import get_input

input = get_input(10)

rows = len(input)
cols = len(input[0])

def find_nines(r, c, num, nines):
    if r >= rows or c >= cols or r < 0 or c < 0 or int(input[r][c]) != num:
        return
    if num == 9:
        nines.append((r,c))
    else:
        find_nines(r+1, c, num+1, nines)
        find_nines(r-1, c, num+1, nines)
        find_nines(r, c+1, num+1, nines)
        find_nines(r, c-1, num+1, nines)

# PARTS 1 and 2

part1, part2 = 0, 0
for r in range(rows):
    for c in range(cols):
        if input[r][c] == "0":
            nines = []
            find_nines(r, c, 0, nines)
            part1 += len(set(nines))
            part2 += len(nines)

print("Part 1:", part1)
print("Part 2:", part2)