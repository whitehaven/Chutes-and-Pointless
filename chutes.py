from random import randrange

from board import no_transit_points as transit_points

BOARDSIZE = 101
DIEMAX = 6
iterations = int(1E5)


def make_move(locus, rounds):
    next_locus = locus + randrange(1, DIEMAX + 1)
    rounds += 1
    if next_locus == BOARDSIZE - 1:
        # hit winning space
        return rounds
    elif next_locus > BOARDSIZE - 1:
        # missed winning space, try again
        return make_move(int(locus), int(rounds))
    elif next_locus in transit_points.keys():
        # hit transit point, move to destination
        next_locus = transit_points[next_locus]
    return make_move(int(next_locus), int(rounds))


round_history = []

for current_iteration in range(0, iterations):
    start_locus = 0
    start_round = 0

    rounds = make_move(start_locus, start_round)

    round_history.append(rounds)

    # print("Trial {iteration:d} took {rounds:d} rounds.".format(iteration=current_iteration + 1, rounds=rounds))

print("Mean rounds: {mean:f}".format(mean=(sum(round_history) / len(round_history))))
print("Max rounds: {max:d}".format(max=max(round_history)))
print("Min rounds: {min:d}".format(min=min(round_history)))
print("Over {iterations:d} iterations".format(iterations=iterations))
