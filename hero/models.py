from django.db import models
from django.core.validators import MinValueValidator

class Hero(models.Model):
    name = models.CharField(max_length=200)
    energy = models.DecimalField(max_digits=15,  decimal_places=4, validators = [MinValueValidator(1.0)], default=0) 
    
class Atributs(models.Model):
    hero = models.OneToOneField(Hero)
    b_pow = models.DecimalField(max_digits=15,  decimal_places=4, validators = [MinValueValidator(1.0)], default=1.0) #base power
    b_rns = models.DecimalField(max_digits=15,  decimal_places=4, validators = [MinValueValidator(1.0)], default=1.0) #base resistans
    b_dex = models.DecimalField(max_digits=15,  decimal_places=4, validators = [MinValueValidator(1.0)], default=1.0) #base dexterity
    b_per = models.DecimalField(max_digits=15,  decimal_places=4, validators = [MinValueValidator(1.0)], default=1.0) #base perception
    b_int = models.DecimalField(max_digits=15,  decimal_places=4, validators = [MinValueValidator(1.0)], default=1.0) #base inteligens
    b_web = models.DecimalField(max_digits=15,  decimal_places=4, validators = [MinValueValidator(1.0)], default=1.0) #base web
    b_rss = models.DecimalField(max_digits=15,  decimal_places=4, validators = [MinValueValidator(1.0)], default=1.0) #base resourcefulness

class Main_stats(models.Model):
    hero = models.OneToOneField(Hero)
    b_hp = models.DecimalField(max_digits=15,  decimal_places=4, validators = [MinValueValidator(1.0)], default=10.0) #Base hit points
    b_ap = models.DecimalField(max_digits=15,  decimal_places=4, validators = [MinValueValidator(1.0)], default=100.0) #base action points
    b_sp = models.DecimalField(max_digits=15,  decimal_places=4, validators = [MinValueValidator(0.001)], default=0.001) #base speed
    
class Ba_skills(models.Model): #Battle skills
    hero = models.OneToOneField(Hero)
    b_hide = models.DecimalField(max_digits=15,  decimal_places=4, validators = [MinValueValidator(0.0)], default=0.0) #Base hide
    b_dete = models.DecimalField(max_digits=15,  decimal_places=4, validators = [MinValueValidator(0.0)], default=0.0) #Base detection
    
class Ba_proficiency(models.Model): #Battle proficiency
    hero = models.OneToOneField(Hero)
    p_mel = models.DecimalField(max_digits=15,  decimal_places=4, validators = [MinValueValidator(0.0)], default=0.0) #melee atackp proficiency
    p_ran = models.DecimalField(max_digits=15,  decimal_places=4, validators = [MinValueValidator(0.0)], default=0.0) #range atack proficiency
    p_pro = models.DecimalField(max_digits=15,  decimal_places=4, validators = [MinValueValidator(0.0)], default=0.0) #programing use proficiency
    p_web = models.DecimalField(max_digits=15,  decimal_places=4, validators = [MinValueValidator(0.0)], default=0.0) #web use proficiency
    p_ant = models.DecimalField(max_digits=15,  decimal_places=4, validators = [MinValueValidator(0.0)], default=0.0) #antiwirus defence proficiency
    p_dod = models.DecimalField(max_digits=15,  decimal_places=4, validators = [MinValueValidator(0.0)], default=0.0) #dodge proficiency
    p_hide = models.DecimalField(max_digits=15,  decimal_places=4, validators = [MinValueValidator(0.0)], default=0.0) #hide proficiency
    p_dete = models.DecimalField(max_digits=15,  decimal_places=4, validators = [MinValueValidator(0.0)], default=0.0) #Detection proficiency
    p_move = models.DecimalField(max_digits=15,  decimal_places=4, validators = [MinValueValidator(1.0)], default=1.0) #Proficiency in quick moves