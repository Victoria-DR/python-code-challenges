from random import randint

def roll_dice(*args):
    possible_outcomes = {i for i in range(len(args), sum(args) + 1)}
    outcomes = {}.fromkeys(possible_outcomes, 0)

    for i in range(1000000):
        roll_sum = 0
        for dice in args:
            roll_sum += randint(1, dice)
        outcomes[roll_sum] += 1

    message = "OUTCOME PROBABILITY"

    for i in range(len(args), sum(args) + 1):
        message += f"\n{i}\t{outcomes[i] / 10000:.2f}%"

    return message

print(roll_dice(4, 6, 6))
