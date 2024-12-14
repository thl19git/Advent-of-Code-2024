from utils import get_input
import re
import time
import os

input = " ".join(get_input(14))

guards = re.findall("p=(\d+),(\d+) v=(-?\d+),(-?\d+)", input)
guards = [[int(i) for i in guard] for guard in guards] #[curr_c, curr_r, delta_c, delta_r]

# PART 1

rows = 103
cols = 101

# Find out where all the guards are
def cost():
    q0, q1, q2, q3 = 0, 0, 0, 0
    for guard in guards:
        if guard[0] < 50:
            if guard[1] < 51:
                q0 += 1
            elif guard[1] > 51:
                q1 += 1
        elif guard[0] > 50:
            if guard[1] < 51:
                q2 += 1
            elif guard[1] > 51:
                q3 += 1
    return q0 * q1 * q2 * q3

def display(t):
    grid = dict()
    for guard in guards:
        grid[(guard[1],guard[0])] = "X"
    for r in range(rows):
        row = ""
        for c in range(cols):
            row += grid.get((r,c), " ")
        print(row)
    print(t+1)
    time.sleep(2)
    os.system("clear")

min_cost = 100000000

for t in range(1000000):
    for guard in guards:
        new_c = (guard[0] + guard[2]) % cols
        new_r = (guard[1] + guard[3]) % rows
        guard[0] = new_c
        guard[1] = new_r
    c = cost()
    if t == 99:
        print("Part 1:", c) # PART 1 IS COST / SAFETY FACTOR AFTER 100 SECONDS
    if c < min_cost:
        min_cost = c
        display(t)

# FOR PART 2, MANUALLY INSPECT OUTPUTS UNTIL THE XMAS TREE APPEARS (AFTER 7709 SECONDS, THE SIXTH PICTURE SHOWN)