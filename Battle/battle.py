# coding=utf-8
__author__ = 'Mati', 'Tyr'

from hero.models import Hero
import random

class Battle :

        distance_attack_cost = 12
        close_attack_cost = 8
        web_attack_cost = 15
        activate_field_cost = 30
        activate_program_cost = 10
        activate_virus_cost = 10
        get_closer_cost = 5


        def init_battle(self):
            distance = random.randrange(1000,100001)
            self.init_equipment()
            self.stack_uno=[]
            self.stack_dos=[]
            init_battle()


        def init_equipment(self):
            #tu zaczną wchodzić statystyki związane z ekwipunkiem, a istniające o wartości z ekwipunku zmodyfikowane, w razie potrzeby.
            energy_def = 0
            pen_def = 0
            hit_def = 0
            net_dodge = 0
            melee_dodge = 0
            dist_dodge = 0

        def determine_current(self):
            #res ap?
            if(self.hero1.ap > self.hero2.ap):
                return [self.hero1,self.hero2]
            else:
                return [self.hero2,self.hero1]

        def request_action(self):
            #ai w obecnej formie
            return random.randrange(0,8)

        def check_timer_events(self):
            #funkcja ma sprawdzac, czy nie kończy się efekt działania ewentualnych efektów w czasie walki
            pass


        def fight(self):
            last_current=None
            while self.hero1.current_hp>0 and self.hero2.current_hp>0:
                [current,enemy] = self.determine_current()
                if(last_current!=None and last_current!=current):
                    self.check_timer_events()
                action = self.request_action(current)
                if action==0:
                    log = self.close_attack(current,enemy)
                elif action==1:
                    log = self.distance_attack(current,enemy)
                elif action==2:
                    log = self.get_closer(current,enemy)
                elif action==3:
                    log = self.activate_virus(current,enemy)
                elif action==4:
                    log = self.activate_program(current,enemy)
                elif action==5:
                    log = self.activate_field(current,enemy)
                elif action==6:
                    log = self.web_attack(current,enemy)
                elif action ==7:
                    log = self.skip(current,enemy)
                elif action ==8:
                    log = self.surrender(current, enemy)
                last_current = current
            self.log_list.append(log)
            self.send_log(log)
            self.add_logs_to_db(self.log_list)




        def add_logs_to_db(self,log_list):
            # tu bedzie cośtam cośtam. Proponuję taki format loga:
            # [current.name, current.hp, current.ap, enemy.name, enemy.hp, enemy.ap, opis_słowny]
            pass



        #disclaimer = wszystkie efekty z ekwipunku pominięto. Niestety, nie ma ekwipunku.
        #UWAGA: DODAĆ KRYTYKI
        def close_attack(self,current,enemy):
            #symulacja kosztu broni
            cost = random.randrange(0,5)
            attack = 0.4 * current.get_static(1) + 0.4 * current.get_static(3) + 0.1 * current.get_static(6) + 0.1 * current.melee_attack
            success = random.randrange(0,101)
            if success < attack:
                #przeciwnik dostaje obrazenia, ale lol - nie ma ekwipunku, wiec dostaje w ryj mocą
                return [current.name, current.health_points, current.action_points-cost, enemy.name, enemy.health_points-current.get_static(1), enemy.action_poits, u'%s atakuje %s za %s obrażeń!'%current.name, enemy.name, current.get_static(1)]
            else:
                return [current.name, current.health_points,current.action_points-cost,enemy.name, enemy.health_points, enemy.action_poits, u'%s nie trafia!'%current.name]

        def distance_attack(self,current,enemy):
            #tak samo jak w close attack
            cost = random.randrange(0,5)
            attack = 0.4 * current.get_static(4) + 0.4 * current.get_static(3) + 0.1 * current.get_static(6) + 0.1 * current.melee_attack
            success = random.randrange(0,101)
            if success < attack:
                #przeciwnik dostaje obrazenia, ale lol - nie ma ekwipunku jako takiego, wiec dostaje w ryj sprawnością. A co tam.
                [current.name, current.health_points, current.action_points-cost, enemy.name, enemy.health_points-current.get_static(4), enemy.action_poits, u'%s atakuje %s za %s obrażeń!'%current.name, enemy.name, current.get_static(4)]
            else:
                return [current.name, current.health_points,current.action_points-cost,enemy.name, enemy.health_points, enemy.action_poits, u'%s strzela w %s, ale nie trafia!'%current.name, enemy.name]

        def get_closer(self,current,enemy):
            cost = current.movement_speed/2 # just cause
            self.distance -= current.movement_speed
            return [current.name, current.health_points,current.action_points-cost,enemy.name, enemy.health_points, enemy.action_poits,u'%s zapierdala %s metrów!'%current.name, current.movement_speed]



        def activate_virus(self,current,enemy):
            cost = random.randrange(0,5)
            temp = random.randrange(1,cost+1) #pula. Co to jest pula?
            boop = 0.7 * current.get_static(5) + 0.2 * current.get_static(6) + 0.1 * current.programming
            contraboop = 0.8 * enemy.get_static(5) + 0.2 * enemy.get_static(6) + 0.1 * enemy.programming
            dice = random.randrange(0,101)
            dice2 = random.randrange(0,101)
            counter = 0 #docelowo ma to być licznik czasu trwania programu. Jak będzie, się zobaczy.
            if dice < boop: #jeżeli nasz faggot zdał test mocy
                virus = current.viruses[current.virus_cursor]
                if virus == None:
                    return u'brak wirusow'
                self.add_program_to_hero(virus,enemy)
                current.virus_cursor+=1
                if(current.virus_cursor>=current.viruses.length):
                    add_program_to_hero(virus,enemy)
                    current.virus_cursor+=1
                if(hero.virus_cursor>=current.viruses.length):
                    current.virus_cursor=0
            else:
                #faggot nie zdał testu. Borze jak przykro
                return u'jak szybciej jedzie, lepiej rozpierdala, czyli oddychanie beztlenowe roślin i etymologia słowa amelnium. %s nawet przypierdolić mocą nie potrafi' % current.name

        def activate_program(self,current,enemy):
            cost = random.randrange(0,5)
            temp = random.randrange(1,cost+1) #pula. Co to jest pula?
            boop = 0.9 * current.get_static(5) + 0.1 * current.programming
            dice = random.randrange(0,101)
            if dice < boop:
                program = current.programs[current.program_cursor]
                if(program == None):
                    return u'brak programow'
                self.add_program_to_hero(current,program)
                current.program_cursor+=1
                if(current.program_cursor>=current.programs.length):
                    current.program_cursor=0
            else:
                return u'Kontemplacje widoku za oknem w pociągach linii kraków - wrocław. Widoki chujowe jak barszcz. Moze dlatego, że jest już ciemno. %s to fag, nie potrafi nawet programu rzucić'% current.name

        def activate_field(self,current):
            cost = random.randrange(0,5)
            temp = random.randrange(1,cost+1) #pula. Co to jest pula?
            boop = 0.9 * current.get_static(5) + 0.1 * current.programming
            dice = random.randrange(0,101)
            if dice < boop:
                field = current.field
                if field == None:
                    return u'brak pola'
                current.is_field_activate = True
                self.add_program_to_hero(current,field)
            else:
                return u'Kontemplacje widoku za oknem w pociągach linii kraków - wrocław. Widoki chujowe jak barszcz. Moze dlatego, że jest już ciemno. %s to fag, nie potrafi nawet programu rzucić'% current.name

        def web_attack(current,enemy):
            pass


        def skip(self,current,enemy):
            current.current_ap = 0

        def surrender(self,current,enemy):
            current.current_hp = 0

        def add_program_to_hero(self,hero,program):
            """"Trzeba sprawdzic kazda statystyke hero czy znajduje sie w program i dodac ja do hero"""
            hero.ability_stack.append((program,program.time)) #dodawanie do stosu umiejetnosci
            # dodawanie umiejetnosci
            if hasattr(program,'melee_attack'):
                hero.melee_attack = hero.melee_attack*(program.melee_atack/100)
            if hasattr(program,'range_attack'):
                hero.range_attack = hero.range_attack*(program.range_attack/100)
            if hasattr(program,'programming'):
                hero.programming = hero.programming*(program.programming/100)
            if hasattr(program,'web_use'):
                hero.web_use = hero.web_use*(program.web_use/100)
            if hasattr(program,'antivirus_use'):
                hero.antivirus_use = hero.antivirus_use*(program.antivirus_use/100)
            if hasattr(program,'dodge'):
                hero.dodge = hero.dodge*(program.dodge/100)
            if hasattr(program,'quick_move'):
                hero.quick_move = hero.quick_move*(program.quick_move/100)
            if hasattr(program,'detection_use'):
                hero.detection_use = hero.detection_use*(program.detection_use/100)
            if hasattr(program,'hide_use'):
                hero.hide_use = hero.hide_use*(program.hide_use/100)
            if hasattr(program,'health_points'):
                hero.health_points = hero.health_points*(program.health_points/100)
            if hasattr(program,'virus_resist'):
                hero.virus_resist = hero.virus_resist*(program.virus_resist/100)
            if hasattr(program,'hiding'):
                hero.hiding = hero.hiding*(program.hiding/100)
            if hasattr(program,'detection'):
                hero.detection = hero.detection*(program.detection/100)
            if hasattr(program,'virus_resist'):
                hero.movement_speed = hero.movement_speed*(program.movement_speed/100)
            if hasattr(program,'virus_resist'):
                hero.weapon_switching_speed_uno = hero.weapon_switching_speed_uno*(program.weapon_switching_speed_uno/100)

        def delete_program_from_hero(self,hero,program):
            hero.ability_stack.remove((program,0))
            #usuwanie bonusow z ability
            if hasattr(program,'melee_attack'):
                hero.melee_attack = hero.melee_attack/(program.melee_atack/100)
            if hasattr(program,'range_attack'):
                hero.range_attack = hero.range_attack/(program.range_attack/100)
            if hasattr(program,'programming'):
                hero.programming = hero.programming/(program.programming/100)
            if hasattr(program,'web_use'):
                hero.web_use = hero.web_use/(program.web_use/100)
            if hasattr(program,'antivirus_use'):
                hero.antivirus_use = hero.antivirus_use/(program.antivirus_use/100)
            if hasattr(program,'dodge'):
                hero.dodge = hero.dodge/(program.dodge/100)
            if hasattr(program,'quick_move'):
                hero.quick_move = hero.quick_move/(program.quick_move/100)
            if hasattr(program,'detection_use'):
                hero.detection_use = hero.detection_use/(program.detection_use/100)
            if hasattr(program,'hide_use'):
                hero.hide_use = hero.hide_use/(program.hide_use/100)
            if hasattr(program,'health_points'):
                hero.health_points = hero.health_points/(program.health_points/100)
            if hasattr(program,'virus_resist'):
                hero.virus_resist = hero.virus_resist/(program.virus_resist/100)
            if hasattr(program,'hiding'):
                hero.hiding = hero.hiding/(program.hiding/100)
            if hasattr(program,'detection'):
                hero.detection = hero.detection/(program.detection/100)
            if hasattr(program,'virus_resist'):
                hero.movement_speed = hero.movement_speed/(program.movement_speed/100)
            if hasattr(program,'virus_resist'):
                hero.weapon_switching_speed_uno = hero.weapon_switching_speed_uno/(program.weapon_switching_speed_uno/100)
            #jeszcze sprawdzanie czy uzyty ability jest polem czy nie
            if program.is_field:
                hero.is_field_activate = False

        def check_timer_events(self):
            for i in xrange(self.hero1.ability_stack):
                (x,y) = self.hero1.ability_stack[i]
                y-=1
                self.hero1.ability_stack[i]=(x,y)
                if y==0:
                    self.delete_program_from_hero(self.hero1,x)

            for i in xrange(self.hero2.ability_stack):
                (x,y) = self.hero1.ability_stack[i]
                y-=1
                self.hero2.ability_stack[i]=(x,y)
                if y==0:
                    self.delete_program_from_hero(self.hero2,x)