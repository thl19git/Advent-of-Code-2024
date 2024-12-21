from utils import get_input
from itertools import permutations
import functools

input = get_input(21, False)

numeric_pad = {
    "7": (0,0),
    "8": (0,1),
    "9": (0,2),
    "4": (1,0),
    "5": (1,1),
    "6": (1,2),
    "1": (2,0),
    "2": (2,1),
    "3": (2,2),
    "0": (3,1),
    "A": (3,2),
}

direction_pad = {
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
}

deltas = {
    ">": (0, 1),
    "<": (0, -1),
    "v": (1, 0),
    "^": (-1, 0)
}

def validate_moves(moves, pos):
    for move in moves:
        pos = (pos[0] + deltas[move][0], pos[1] + deltas[move][1])
        if pos not in list(numeric_pad.values()):
            return False
    return True

def find_best_move(moves):
    best_move = None
    best_move_score = -1
    for move in moves:
        move_score = 0
        for i in range(1, len(move)):
            move_score += move[i] == move[i-1]
        if move_score > best_move_score:
            best_move_score = move_score
            best_move = move
        elif move_score == best_move_score:
            for i in range(len(move)):
                if move[i] == best_move[i]:
                    continue
                done = False
                for m in "<v^^":
                    if move[i] == m:
                        best_move = move
                        done = True
                        break
                    if best_move[i] == m:
                        done = True
                        break
                if done:
                    break
    return best_move


def numpad_robot(code):
    move = ""
    pos = (3,2)
    for target in code:
        target_pos = numeric_pad[target]
        if target_pos == pos:
            best_move = "A"
        else:
            dr, dc = target_pos[0] - pos[0], target_pos[1] - pos[1]
            moves = ""
            for _ in range(abs(dr)):
                moves += "v" if dr > 0 else "^"
            for _ in range(abs(dc)):
                moves += ">" if dc > 0 else "<"
            all_moves = {"".join(p) for p in permutations(moves)}
            moves = [m+"A" for m in all_moves if validate_moves(m, pos)]
            best_move = find_best_move(moves)
        move += best_move
        pos = target_pos
    return move

move_matrix = {
    "A": {
        "A": "A",
        "^": "<A",
        "v": "<vA",
        "<": "v<<A",
        ">": "vA",
    },
    "^": {
        "A": ">A",
        "^": "A",
        "v": "vA",
        "<": "v<A",
        ">": "v>A",
    },
    "v": {
        "A": "^>A",
        "^": "^A",
        "v": "A",
        "<": "<A",
        ">": ">A",
    },
    "<": {
        "A": ">>^A",
        "^": ">^A",
        "v": ">A",
        "<": "A",
        ">": ">>A",
    },
    ">": {
        "A": "^A",
        "^": "<^A",
        "v": "<A",
        "<": "<<A",
        ">": "A",
    }
}

@functools.cache
def directional_robot(start, end, num_bots):
    global all_moves
    moves = move_matrix[start][end]
    if num_bots == 1:
        return len(moves)
    num_moves = 0
    pos = "A"
    for move in moves:
        num_moves += directional_robot(pos, move, num_bots-1)
        pos = move
    return num_moves

def get_moves(num_bots):
    answer = 0
    for code in input:
        initial_moves = numpad_robot(code)
        total_moves = 0
        pos = "A"
        for move in initial_moves:
            total_moves += directional_robot(pos, move, num_bots)
            pos = move
        answer += int(code[:-1]) * total_moves
    return answer

print("Part 1:", get_moves(2))
print("Part 2:", get_moves(25))