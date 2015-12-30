from random import randrange

from board import game_1_transit_points

BOARDSIZE = 101
DIEMAX = 6
iterations = 1


def make_move(locus, rounds):
    next_locus = randrange(0, DIEMAX)
    rounds += 1
    if locus + next_locus > BOARDSIZE - 1:
        # missed winning space, try again
        return make_move(locus, rounds)
    elif locus == BOARDSIZE - 1:
        # hit winning space
        return rounds
    elif locus in game_1_transit_points.keys():
        # hit transit point, move to destination
        locus = game_1_transit_points[locus]
    return make_move(next_locus, rounds)


for current_iteration in range(0, iterations):
    print("Trial {iteration:d}".format(iteration=current_iteration + 1))

    start_locus = 0
    start_round = 0

    rounds = make_move(start_locus, start_round)
