from utils import get_input

input = [int(n) for n in get_input(11, False)[0].split()]

def blink(balls, num_blinks):
    for _ in range(num_blinks):
        new_balls = {}
        for ball, count in balls.items():
            if ball == 0:
                if 1 not in new_balls:
                    new_balls[1] = 0
                new_balls[1] += count
            elif len(str(ball)) % 2 == 0:
                left = int(str(ball)[:len(str(ball))//2])
                right = int(str(ball)[len(str(ball))//2:])
                if left not in new_balls:
                    new_balls[left] = 0
                new_balls[left] += count
                if right not in new_balls:
                    new_balls[right] = 0
                new_balls[right] += count
            else:
                new_ball = ball * 2024
                if new_ball not in new_balls:
                    new_balls[new_ball] = 0
                new_balls[new_ball] += count
        balls = new_balls
    return balls

# PART 1

balls = {ball: 1 for ball in input}
balls_1 = blink(balls, 25)
print("Part 1:", sum(list(balls_1.values())))

# PART 2

balls_2 = blink(balls_1, 50)
print("Part 2:", sum(list(balls_2.values())))