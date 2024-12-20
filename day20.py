from utils import get_input

input = get_input(20, False)

track = {}

start = None
end = None

for r, row in enumerate(input):
    for c, el in enumerate(row):
        track[complex(r,c)] = el
        if el == "S":
            start = complex(r,c)
        elif el == "E":
            end = complex(r,c)

threshold = 100
cheats = 0

pos = end
steps = 0

while True:
    track[pos] = steps
    for jump in [2, -2, 2j, -2j]:
        val = track.get(pos + jump, "#")
        if type(val) is int:
            if (steps - val) >= (threshold + 2):
                cheats += 1
    if pos == start:
        break
    for move in [1, -1, 1j, -1j]:
        if track.get(pos + move, "#") in [".", "S"]:
            pos += move
            steps += 1
            break

print("Part 1:", cheats)

pos = end
steps = 0
cheats2 = 0

def find_cheats(pos):
    steps = track[pos]
    cheats = 0
    for r in range(-20,21):
        for c in range(abs(r)-20,21-abs(r)):
            move = complex(r,c)
            val = track.get(pos + move, "#")
            if type(val) is int and (steps - val - abs(r) - abs(c)) >= threshold:
                cheats += 1
    return cheats

while True:
    if steps >=100:
        # Search for cheats
        cheats2 += find_cheats(pos)
    if pos == start:
        break
    for move in [1, -1, 1j, -1j]:
        if type(track.get(pos + move, "#")) is int and track[pos + move] > track[pos]:
            pos += move
            steps += 1
            break

print("Part 2:", cheats2)