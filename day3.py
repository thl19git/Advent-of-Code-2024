from utils import get_input
import re

input = get_input(3)

def sum_section(section):
    res = 0
    muls = re.findall("mul\([0-9]+,[0-9]+\)", section)
    for mul in muls:
        num1 = int(mul.split(",")[0][4:])
        num2 = int(mul.split(",")[1][:-1])
        res += num1 * num2
    return res

# PART 1

part1 = 0
for line in input:
    part1 += sum_section(line)

# PART 2

all_input = "".join(input)
donts = all_input.split("don't()")
part2 = sum_section(donts[0])
for dont in donts[1:]:
    if "do()" not in dont:
        continue
    do = "".join(dont.split("do()")[1:])
    part2 += sum_section(do)

print("Part 1:", part1)
print("Part 2:", part2)