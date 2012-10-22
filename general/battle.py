__author__ = 'Tyr', 'Mati'
import random

#AI w obecnej formie.
def request_action(player):
    return random.randrange(0,7)


def battle(hero_id1, hero_id2):
    logs = ""
