from utils import get_input
import numpy as np

input = get_input(13, False)

problems = []

problem = {}
for line in input:
    if line == "":
        problems.append(problem)
        problem = {}
    elif "Button A" in line or "Button B" in line:
        problem[line[7]] = (int(line[12:14]),int(line[18:20]))
    else:
        x = int(line.split(":")[1].split(",")[0].strip()[2:])
        y = int(line.split(",")[1].strip()[2:])
        problem["Prize"] = (x,y)
if problem:
    problems.append(problem)

# PART 1

part1 = 0
for problem in problems:
    A = np.array([[problem["A"][0], problem["B"][0]], [problem["A"][1], problem["B"][1]]])
    B = np.array([[problem["Prize"][0]], [problem["Prize"][1]]])
    sol = np.linalg.inv(A) @ B
    if np.all(np.isclose(sol, np.round(sol), 0.0000001)) and np.all(sol >= 0):
        part1 += 3 * sol[0] + sol[1]

print("Part 1:", part1)

# PART 2

part2 = 0
for problem in problems:
    A = np.array([[problem["A"][0], problem["B"][0]], [problem["A"][1], problem["B"][1]]])
    B = np.array([[problem["Prize"][0] + 10000000000000], [problem["Prize"][1] + 10000000000000]])
    sol = np.linalg.inv(A) @ B
    if np.all(np.isclose(sol, np.round(sol), 0.000000000000001)) and np.all(sol >= 0):
        part2 += 3 * np.round(sol[0]) + np.round(sol[1])

np.set_printoptions(precision=15)

print("Part 2:", part2)