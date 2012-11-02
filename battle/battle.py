# coding=utf-8
__author__ = 'Mati', 'Tyr'

from hero.models import Hero
import random

class Battle :
        distance = 0
        distance_attack_cost = 12
        close_attack_cost = 8
        web_attack_cost = 15
        activate_field_cost = 30
        activate_program_cost = 10
        activate_virus_cost = 10
        get_closer_cost = 5

        #gicior
        def __init__(self,hero1_id,hero2_id):
            #dlaczego, do ciężkiej cholery, nie resolvuje objects?
            self.hero1 = Hero.objects.get(id = hero1_id)
            self.hero2 = Hero.objects.get(id = hero2_id)
            self.log_list=[]
            self.init_battle()

        #wunderbar
        def init_battle(self):
            distance = random.randrange(1000,100001)
            self.init_equipment()
            self.stack_uno=[]
            self.stack_dos=[]
            #tak, silly python, istnieje taka metoda jak init_equipement()
            init_equipement()


        #zjebane. Trzeba to wypierdolic
        def init_equipment(self):
            #tu zaczną wchodzić statystyki związane z ekwipunkiem, a istniające o wartości z ekwipunku zmodyfikowane, w razie potrzeby.
            #TODO: zasadniczo to powinno byc w hero. Albo inicjalnie dac dla dwóch graczy i, łopatopogicznie, uno dos.
            energy_def = 0
            pen_def = 0
            hit_def = 0
            net_dodge = 0
            melee_dodge = 0
            dist_dodge = 0


        #wybdabar
        def determine_current(self):
            #res ap?
            if(self.hero1.current_ap > self.hero2.current_ap):
                return [self.hero1,self.hero2]
            else:
                return [self.hero2,self.hero1]

        #pewnie, ze wszystko done.
        def request_action(self):
            #ai w obecnej formie
            return random.randrange(0,9)


        #wspaniałe
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



        #ogolnie dobrze, tylko po pętli trzeba jebnąć podsumowanie walki, finalny log i gra muzyka
        #a, jescze rozwarzyć koncept zapisywania życia wygranego po walce -  tak, żeby był osłabiony
        def fight(self):
            last_current=None
            log = []
            while self.hero1.current_hp>0 and self.hero2.current_hp>0:
                [current,enemy] = self.determine_current()
                if(last_current!=None and last_current!=current):
                    last_current.current_ap = last_current.ap
                    self.check_timer_events()
                action = self.request_action()
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
            #co to kurwa jest.
            #self.send_log(log)

            # w sumie to jest kurna niepotrzebne
            #self.add_logs_to_db(self.log_list)




#        def add_logs_to_db(self,log_list):
#            # tu bedzie cośtam cośtam. Proponuję taki format loga:
#            # [current.name, current.hp, current.ap, enemy.name, enemy.hp, enemy.ap, opis_słowny]
#            pass



        #disclaimer = wszystkie efekty z ekwipunku pominięto. Niestety, nie ma ekwipunku.
        #UWAGA: DODAĆ KRYTYKI

        #zrobione wszystko poza ekwipunkiem i krytykiem, nieprzekonwertowane
        def close_attack(self,current,enemy):
            #symulacja kosztu broni
            cost = random.randrange(0,5)
            attack = 0.4 * current.get_static(1) + 0.4 * current.get_static(3) + 0.1 * current.get_static(6) + 0.1 * current.melee_attack
            success = random.randrange(0,101)
            if success < attack:
                #przeciwnik dostaje obrazenia, ale lol - nie ma ekwipunku, wiec dostaje w ryj mocą
                current.current_ap -= cost
                enemy.current_hp -= current.get_static(1)
                return [current.name, current.current_hp, current.current_ap, enemy.name,
                        enemy.current_hp, enemy.current_ap, u'%s atakuje %s za %s obrażeń!'%current.name, enemy.name, current.get_static(1)]
            else:
                current.current_ap -= cost
                return [current.name, current.current_hp, current.current_ap, enemy.name,
                        enemy.current_hp, enemy.current_ap, u'%s nie trafia!'%current.name]


        #zrobione wszystko poza ekwipunkiem i krytykiem, nieprzekonwertowane
        def distance_attack(self,current,enemy):
            cost = random.randrange(0,5)
            attack = 0.4 * current.get_static(4) + 0.4 * current.get_static(3) + 0.1 * current.get_static(6) + 0.1 * current.melee_attack
            success = random.randrange(0,101)
            if success < attack:
                #przeciwnik dostaje obrazenia, ale lol - nie ma ekwipunku jako takiego, wiec dostaje w ryj sprawnością. A co tam.
                current.current_ap -= cost
                enemy.current_hp -= current.get_static(4)
                return [current.name, current.current_hp, current.current_ap, enemy.name,enemy.current_hp, enemy.current_ap,
                        u'%s atakuje %s za %s obrażeń!'%current.name, enemy.name, current.get_static(4)]
            else:
                current.current_ap -= cost
                return [current.name, current.current_hp, current.current_ap, enemy.name,enemy.current_hp,
                        enemy.current_ap, u'%s strzela w %s, ale nie trafia!'%current.name, enemy.name]

        #zrobione wszystko, nieprzekonwertowane
        def get_closer(self,current,enemy):
            cost = current.movement_speed/2 # just cause
            self.distance -= current.movement_speed
            current.current_ap -= cost
            return [current.name, current.current_hp, current.current_ap, enemy.name,enemy.current_hp, enemy.current_ap,
                    u'%s zapierdala %s metrów!'%current.name, current.movement_speed]

        #nie mam kurwa pojęcia. Ale chyba dobrze. Nieprzekonwertowane
        def activate_virus(self,current,enemy):
            cost = random.randrange(0,5)
            temp = random.randrange(1,cost+1) #pula. Co to jest pula?
            boop = 0.7 * current.get_static(5) + 0.2 * current.get_static(6) + 0.1 * current.programming
            contraboop = 0.8 * enemy.get_static(5) + 0.2 * enemy.get_static(6) + 0.1 * enemy.programming
            dice = random.randrange(0,101)
            dice2 = random.randrange(0,101)
            #zasadniczo to dzialka matiego, ale chyba jest dobrze. W takim razie to potrzebne?
            counter = 0 #docelowo ma to być licznik czasu trwania programu. Jak będzie, się zobaczy.
            if dice < boop: #jeżeli nasz faggot zdał test mocy
                virus = current.viruses[current.virus_cursor]
                if virus is None:
                    current.current_ap -= cost #dobrze?
                    return [current.name, current.current_hp, current.current_ap, enemy.name,enemy.current_hp, enemy.current_ap,u'brak wirusow']
                self.add_program_to_hero(virus,enemy)
                current.virus_cursor+=1
                if current.virus_cursor>=current.viruses.length:
                    add_program_to_hero(virus,enemy)
                    current.virus_cursor+=1
                #co to kurwa jest \/
                if hero.virus_cursor>=current.viruses.length:
                    current.virus_cursor=0
            else:
                #faggot nie zdał testu. Borze jak przykro
                current.current_ap -= cost
                return [current.name, current.current_hp, current.current_ap, enemy.name,enemy.current_hp, enemy.current_ap,
                        u'jak szybciej jedzie, lepiej rozpierdala, czyli oddychanie beztlenowe roślin i etymologia słowa amelnium. %s nawet przypierdolić mocą nie potrafi' % current.name]


       #cos tu jest kurwa nie wporzadku. Nie podoba mi sie to.
        def activate_program(self,current,enemy):
            cost = random.randrange(0,5)
            temp = random.randrange(1,cost+1) #pula. Co to jest pula?
            boop = 0.9 * current.get_static(5) + 0.1 * current.programming
            dice = random.randrange(0,101)
            if dice < boop:
                program = current.programs[current.program_cursor]
                if program is None:
                    add_program_to_hero(current,program)
                    current.program_cursor+=1
                    return [current.name, current.current_hp, current.current_ap, enemy.name,enemy.current_hp, enemy.current_ap,u'brak programow']
                if current.program_cursor>=current.programs.length:
                    current.program_cursor=0
            else:
                current.current_ap -= cost
                return [current.name, current.current_hp, current.current_ap, enemy.name,enemy.current_hp, enemy.current_ap,
                        u'Kontemplacje widoku za oknem w pociągach linii kraków - wrocław. Widoki chujowe jak barszcz. Moze dlatego, że jest już ciemno. '
                        u'%s to fag, nie potrafi nawet programu rzucić'% current.name]


        #do sprawdzenia, ale chyba dobrze. Nieprzekonwertowane.
        def activate_field(self,current, enemy):
            cost = random.randrange(0,5)
            temp = random.randrange(1,cost+1) #pula. Co to jest pula?
            boop = 0.9 * current.get_static(5) + 0.1 * current.programming
            dice = random.randrange(0,101)
            if dice < boop:
                field = current.field
                if field is None:
                    return u'brak pola'
                current.is_field_activate = True
                self.add_program_to_hero(current,field)
                current.current_ap -= cost
                return [current.name, current.current_hp, current.current_ap, enemy.name,enemy.current_hp, enemy.current_ap,
                        u'%s rzuca pole...tak?'% current.name]
            else:
                current.current_ap -= cost
                return [current.name, current.current_hp, current.current_ap, enemy.name,enemy.current_hp, enemy.current_ap,
                u'Kontemplacje widoku za oknem w pociągach linii kraków - wrocław. Widoki chujowe jak barszcz.'
                u' Moze dlatego, że jest już ciemno. %s to fag, nie potrafi nawet programu rzucić'% current.name]

        #done and resolved poza eq i krytykiem...jesli jakis bedzie. Znow, kwestia balansu.
        def web_attack(self,current,enemy):
            #zmieniamy forme web - bedzie po prostu atakiem z innych statsow, nie wymagajacym ladowania. Kwestie balansu
            #przedstawie na konferencji
            cost = random.randrange(0,5)
            boop = current.get_updated_web() * 0.4 + current.get_updated_intelligence() * 0.2 +\
                   current.get_updated_perception() * 0.2 + current.web_use * 0.1
            dice = random.randrange(0,101)
            da_dmg = random.randrange(0, cost+1000)
            if dice < boop:
                current.current_ap -= cost
                enemy.current_hp -= da_dmg
                return [current.name, current.current_hp, current.current_ap, enemy.name,enemy.current_hp, enemy.current_ap,
                        u'%s przypierdolil w %s internetami!'%current.name, enemy.name]
            else:
                current.current_ap -= cost
                return [current.name, current.current_hp, current.current_ap, enemy.name,enemy.current_hp, enemy.current_ap,
                        u'%s nie trafił w %s kotem!'%current.name, enemy.name]


        #dun.
        def skip(self,current,enemy):
            current.current_ap = 0
            return [current.name, current.current_hp, current.current_ap, enemy.name,enemy.current_hp, enemy.current_ap,
                    u'%s jest przyczajonym tygrysem. Tutaj nawet kurwa nie staram sie byc smiesznym'% current.name]

        #lol, dun!
        def surrender(self,current,enemy):
            current.current_hp = 0
            return [current.name, current.current_hp, current.current_ap, enemy.name,enemy.current_hp, enemy.current_ap,
             u'%s poddaje walkę jak ostatnia pizda!'% current.name]

        #huh?
        def add_program_to_hero(self,hero,program):
            """"Trzeba sprawdzic kazda statystyke hero czy znajduje sie w program i dodac ja do hero"""
            hero.ability_stack.append((program,program.time)) #dodawanie do stosu umiejetnosci
            # dodawanie umiejętności
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


        #pam pam param pam pam
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

