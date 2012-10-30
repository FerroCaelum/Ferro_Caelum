__author__ = 'Mati'

from hero.models import Hero
import random

class Battle :
    def __init__(self,hero1,hero2):
        self.hero1 = hero1.clone()
        self.hero2 = hero2.clone()
        self.log_list=[];
        init_battle()

    def init_battle(self):
        self.distance = random.randrange(10,101)

    def fight(self):

        while self.hero1.hp>0 and self.hero2.hp>0:
            [current,enemy] = determine_current()
            action = request_action(current)

            if action==0:
                log = close_attack(current,enemy)
            elif action==1:
                log = distance_attack(current,enemy)
            elif action==2:
                log = get_closer(current,enemy)
            elif action==3:
                log = activate_virus(current,enemy)
            elif action==4:
                log = activate_program(current,enemy)
            elif action==5:
                log = activate_field(current,enemy)
            elif action==6:
                log = web_attack(current,enemy)
            self.log_list.append(log)
            send_log(log)
        add_logs_to_db(self.log_list)

    def determine_current(self):
        if(self.hero1.ap>self.hero2.ap):
            return [self.hero1,self.hero2]
        else:
            return [self.hero2,self.hero1]

    def add_logs_to_db(self,log_list):
        pass

    def request_action(self):
        pass

    def close_attack(self,current,enemy):
        pass

    def distance_attack(self,current,enemy):
        pass

    def get_closer(self,current,enemy):
        pass

    def activate_virus(self,current,enemy):
        pass

    def activate_program(self,current,enemy):
        pass

    def activate_field(current,enemy):
        pass

    def web_attack(current,enemy):
        pass