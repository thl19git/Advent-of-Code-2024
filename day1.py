from utils import get_input
from collections import Counter

input = get_input(1)

left = []
right = []

for line in input:
    parts = line.split()
    left.append(int(parts[0]))
    right.append(int(parts[1]))

# PART 1

diff = 0

for l, r in zip(sorted(left), sorted(right)):
    diff += abs(l-r)

print("Part 1:", diff)

# PART 2

counts = Counter(right)

sum = 0

for l in left:
    sum += l * counts[l]

print("Part 2:", sum)