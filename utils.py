def get_input(day, test=False):
    file = "inputs/day" + str(day) + ("_test.txt" if test else ".txt")
    with open(file, "r") as f:
        return [l.strip() for l in f.readlines()]