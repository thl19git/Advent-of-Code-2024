from utils import get_input

input = get_input(7)

def possible(target, nums, part2=False):
    if len(nums) == 2:
        return nums[0] * nums[1] == target or nums[0] + nums[1] == target or (part2 and (int(str(nums[0]) + str(nums[1])) == target))
    return possible(target, [nums[0] * nums[1]] + nums[2:], part2) or possible(target, [nums[0] + nums[1]] + nums[2:], part2) or (part2 and possible(target, [int(str(nums[0]) + str(nums[1]))] + nums[2:], part2))

# PARTS 1 and 2

part1, part2 = 0, 0
for row in input:
    target = int(row.split(":")[0])
    nums = [int(n.strip()) for n in row.split(":")[1].split()]
    part1 += possible(target, nums) * target
    part2 += possible(target, nums, part2=True) * target

print("Part 1:", part1)
print("Part 2:", part2)