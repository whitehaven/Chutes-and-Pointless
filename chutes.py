from random import randrange
from sys import setrecursionlimit

from board import game_1_transit_points

BOARDSIZE = 101
DIEMAX = 6
iterations = 1


def make_move(locus, rounds):
    next_locus = locus + randrange(1, DIEMAX + 1)
    rounds += 1
    if next_locus == BOARDSIZE - 1:
        # hit winning space
        return rounds
    elif next_locus > BOARDSIZE - 1:
        # missed winning space, try again
        return make_move(int(locus), int(rounds))
    elif next_locus in game_1_transit_points.keys():
        # hit transit point, move to destination
        next_locus = game_1_transit_points[next_locus]
    return make_move(int(next_locus), int(rounds))


setrecursionlimit(2000)

for current_iteration in range(0, iterations):
    start_locus = 0
    start_round = 0

    rounds = make_move(start_locus, start_round)

    print("Trial {iteration:d} took {rounds:d} rounds.".format(iteration=current_iteration + 1, rounds=rounds))
