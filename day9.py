from utils import get_input

input = [int(n) for n in get_input(9, False)[0]]

# PART 1

part1 = 0

i = 0
j = len(input) - 1
pos = 0
remaining_j = input[j]
remaining_i = 0

while i < j:
    if i % 2 == 0:
        for k in range(input[i]):
            part1 += (i // 2) * pos
            pos += 1
        i += 1
        remaining_i = input[i]
    else:
        for k in range(min(remaining_i, remaining_j)):
            part1 += (j // 2) * pos
            pos += 1
            remaining_i -= 1
            remaining_j -= 1
        if remaining_i == 0:
            i += 1
        if remaining_j == 0:
            j -= 2
            remaining_j = input[j]

if remaining_j and not remaining_i:
    for k in range(remaining_j):
        part1 += (j // 2) * pos
        pos += 1

# PART 2

expanded_input = []

for i, val in enumerate(input):
    if i % 2 == 0:
        expanded_input.extend([i//2]*val)
    else:
        expanded_input.extend([-1]*val)

j = len(expanded_input) -  1

while j > 0:
    start_j = j
    while expanded_input[j-1] == expanded_input[j]:
        j -= 1
    length = start_j - j + 1
    i = 0
    curr_len = 0
    while i < j:
        if expanded_input[i] == -1:
            curr_len += 1
            if curr_len == length:
                value = expanded_input[j]
                for k in range(length):
                    expanded_input[i-k] = value
                    expanded_input[j+k] = -1
                break
            else:
                i += 1
        else:
            curr_len = 0
            i += 1
    if i == j:
        j -= 1
    while expanded_input[j] == -1:
        j -= 1

part2 = 0
for i, val in enumerate(expanded_input):
    if val != -1:
        part2 += i * val

print("Part 1:", part1)
print("Part 2:", part2)