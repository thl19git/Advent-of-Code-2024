from utils import get_input

input = get_input(4)

# PART 1

xmas = "XMAS"
directions = [(0,1),(1,0),(0,-1),(-1,0),(1,-1),(1,1),(-1,1),(-1,-1)]

def search_for_letter(r, c, dir, letter_index):
    r += dir[0]
    c += dir[1]

    if r < 0 or r >= len(input) or c < 0 or c >= len(input[0]):
        return 0 # out of bounds
    
    if input[r][c] != xmas[letter_index]:
        return 0 # wrong letter
    
    if letter_index == 3:
        return 1 # found the S, word complete
    
    return search_for_letter(r, c, dir, letter_index+1) # continue search for rest of word

def search_from_position(r, c):
    if input[r][c] != "X":
        return 0 # only start searching from X
    count = 0
    for dir in directions:
        count += search_for_letter(r, c, dir, 1)
    return count

part1 = 0
for r in range(len(input)):
    for c in range(len(input[0])):
        part1 += search_from_position(r, c)

# PART 2

def search_letter(r, c, letter):
    if r < 0 or r >= len(input) or c < 0 or c >= len(input[0]):
        return False
    return input[r][c] == letter

def search_diagonal(r, c, dir):
    if search_letter(r+dir[0], c+dir[1], "M") and search_letter(r-dir[0], c-dir[1], "S"):
        return True
    if search_letter(r+dir[0], c+dir[1], "S") and search_letter(r-dir[0], c-dir[1], "M"):
        return True
    return False

def search_from_position_2(r, c):
    if input[r][c] != "A":
        return 0 # only start searching from A
    if search_diagonal(r, c, (1,1)) and search_diagonal(r, c, (-1,1)):
        return 1 # found an XMAS
    return 0

part2 = 0
for r in range(len(input)):
    for c in range(len(input[0])):
        part2 += search_from_position_2(r, c)

print("Part 1:", part1)
print("Part 2:", part2)