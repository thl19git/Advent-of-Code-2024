from utils import get_input
import math

input = get_input(8, False)

antenna = {}

rows = len(input)
cols = len(input[0])

def in_bounds(r, c):
    return r >= 0 and r < rows and c >= 0 and c < cols

for r in range(rows):
    for c in range(cols):
        value = input[r][c]
        if value == ".":
            continue
        if value in antenna:
            antenna[value].append((r,c))
        else:
            antenna[value] = [(r,c)]

# PART 1

antinodes1 = set()
for value, positions in antenna.items():
    for i in range(len(positions)):
        pos1 = positions[i]
        for j in range(i+1, len(positions)):
            pos2 = positions[j]
            diff = (pos2[0]-pos1[0],pos2[1]-pos1[1])
            # Try the two outer ones:
            outer1 = (pos1[0]-diff[0],pos1[1]-diff[1])
            if in_bounds(outer1[0], outer1[1]):
                antinodes1.add(outer1)
            outer2 = (pos2[0]+diff[0],pos2[1]+diff[1])
            if in_bounds(outer2[0], outer2[1]):
                antinodes1.add(outer2)
            # Try the two inner ones:
            inner1 = (pos1[0]+2*diff[0]/3,pos1[1]+2*diff[1]/3)
            if inner1[0] % 1 == 0 and inner1[1] % 1 == 0:
                antinodes1.add(inner1)
            inner2 = (pos1[0]+diff[0]/3,pos1[1]+diff[1]/3)
            if inner2[0] % 1 == 0 and inner2[1] % 1 == 0:
                antinodes1.add(inner2)

# PART 2

antinodes2 = set()
for value, positions in antenna.items():
    for i in range(len(positions)):
        pos1 = positions[i]
        for j in range(i+1, len(positions)):
            pos2 = positions[j]
            diff = (pos2[0]-pos1[0],pos2[1]-pos1[1])
            gcd = math.gcd(abs(diff[0]), abs(diff[1]))
            diff = (diff[0]//gcd,diff[1]//gcd)
            m = 0
            while True:
                new_pos = (pos1[0]+m*diff[0],pos1[1]+m*diff[1])
                if in_bounds(new_pos[0], new_pos[1]):
                    antinodes2.add(new_pos)
                    m -= 1
                else:
                    break
            m = 1
            while True:
                new_pos = (pos1[0]+m*diff[0],pos1[1]+m*diff[1])
                if in_bounds(new_pos[0], new_pos[1]):
                    antinodes2.add(new_pos)
                    m += 1
                else:
                    break

print("Part 1:", len(antinodes1))
print("Part 2:", len(antinodes2))