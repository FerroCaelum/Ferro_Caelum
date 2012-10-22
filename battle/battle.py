__author__ = 'Mati', 'Tyr'
import random


class Battle :
    def __init__(self,hero1,hero2):
        self.__hero1 = hero1
        self.__hero2 = hero2
        init_heroes

    def init_heroes(self):
        pass



    #AI w obecnej formie.
    def request_action(player):
        return random.randrange(0,7)


