from utils import get_input

input = get_input(5, False)

# PART 1

before = {}

i = 0
while input[i] != "":
    line = input[i]
    parts = line.split("|")
    first = int(parts[0])
    second = int(parts[1])
    if second not in before:
        before[second] = {first}
    else:
        before[second].add(first)
    i += 1

i += 1 # skip the empty line

unordered = [] # for part 2!!

result = 0
while i < len(input):
    bad_pages = set()
    good_order = True
    pages = [int(page) for page in input[i].split(",")]
    for page in pages:
        if page in bad_pages:
            good_order = False
            break
        bad_pages = bad_pages.union(before.get(page, set()))
    if good_order:
        result += pages[(len(pages) - 1) // 2]
    else:
        unordered.append(pages)
    i += 1

print("Part 1:", result)

# PART 2

result = 0
for pages in unordered:
    for page in pages:
        if len(set(pages).intersection(before[page])) == (len(pages)-1)//2:
            result += page
            break

print("Part 2:", result)

