# coding: utf-8
from django.db import models
import armory.models
from blood_line.models import BloodLine
from profession.models import Profession
from talent.models import Talent

class Owner(models.Model):
    # Nazwa np. Rycerz Tomek, Sklepikarz z Aden, Jurand ze Spychowa, etc
    name = models.CharField(max_length=50)

    # Level
    lvl = models.PositiveIntegerField(default=1)

    # Max udźwig
    max_load = models.BigIntegerField()

    # Obecny udźwig
    load = models.BigIntegerField()

    def give(self, itemInstance, new_owner, count):
        """Przekazuje item nowemu właścicielowi."""
        assert itemInstance is armory.models.ItemInstance
        assert new_owner is Owner
        assert count is int

        if not itemInstance.item.tradeable:# czy itemem można handlować?
            raise Exception(u'%s is not tradeable.' % self.name)
        if itemInstance.owner != self: # czy item należy do mnie?
            raise Exception(u'Cannot give not yours item.')

        if itemInstance.count < count: # czy mam wystarczająco dużo itema?
            raise Exception(u'%s cannot give more than they have of %s.' % self.name,
                itemInstance.item.name)
        itemInstance.count -= count # zabieramy item sobie
        itemInstance.item.spawn(count, new_owner) # spawnujemy u nowego właściciela

    def item(self, location):
        """
        Zwraca item, który znajduje się w location.
        Wywołanie: owner.item("LeftHand")
        """
        items = armory.models.ItemInstance.objects.filter(owner=self)
        location_flag = armory.models.ItemInstance.LOCATION_FLAGS[location]
        for item in items:
            if item.location & location_flag == location_flag:
                return item
        return None

    def __unicode__(self):
        return u'%s' % self.name


class Hero(Owner):
    lvl_points = models.PositiveIntegerField(default=100)
    blood_line = models.ForeignKey(BloodLine, null=True)
    profession = models.ForeignKey(Profession, null=True)
    experience = models.PositiveIntegerField(default=0)
    talent = models.ManyToManyField(Talent, null=True)
    energy = models.BigIntegerField()
    #atrybuty
    energy_regeneration = models.BigIntegerField()
    power = models.BigIntegerField() #moc
    resistance = models.BigIntegerField() #wytrzymałość
    dexterity = models.BigIntegerField() #sprawność
    perception = models.BigIntegerField() #percepcja
    intelligence = models.BigIntegerField() #inteligencja
    web = models.BigIntegerField() #sieć
    artifice = models.BigIntegerField() #spryt
    #statystyki główne
    hp = models.BigIntegerField() #punkty życia
    ap = models.BigIntegerField() #punkty akcji
    speed = models.BigIntegerField() #prędkość
    #umiejętności
    detection = models.PositiveIntegerField(default=0) #detekcja
    hide = models.PositiveIntegerField(default=0) #kamuflaż
    trade = models.PositiveIntegerField(default=0) #handel

    #>Bojowe
    #    melee_attack = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #atak wręcz
    #    range_attack = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #atak dystansowy
    #    programming = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #programowanie
    #    web_use = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #używanie sieci
    #    antivirus_use = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #obrona antywirusowa
    #    dodge = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #uniki
    #    quick_move = models.DecimalField(max_digits=10, decimal_places=4, validators=[MinValueValidator(0.0)], default=0.0) #szybkie poruszanie się
    #    Powód wykomentowania:
    #    TODO Statystyki bojowe są używane i wyliczane tylko podczas walki. Przenieść do battle.

    #>Umiejętności:
    detection_use = models.DecimalField(max_digits=10, decimal_places=4, default=0.0) #wykrywanie
    hide_use = models.DecimalField(max_digits=10, decimal_places=4, default=0.0) #ukrywanie się
    trade_use = models.DecimalField(max_digits=10, decimal_places=4, default=0.0) #handlowanie

    def equip(self, itemInstance, location):
        """Zakłada item"""
        assert itemInstance is armory.models.ItemInstance
        assert location is str

        if itemInstance.owner != self:
            raise Exception(u'Cannot equip not ur item.')
        itemInstance.location = armory.models.ItemInstance.LOCATION_FLAGS[location]

    def take_off(self, itemInstance):
        """Zdejmuje item"""
        assert itemInstance is armory.models.ItemInstance

        if itemInstance.owner != self:
            raise Exception(u'Cannot take off not ur item.')
        itemInstance.location = None

    def get_statistic(self, number):
        """Metoda zwracająca wartość statystyki o podanym numerze. UWAGA: metoda niekompletna"""
        if number == 1:
            return self.power
        if number == 2:
            return self.resistance
        if number == 3:
            return self.dexterity
        if number == 4:
            return self.perception
        if number == 5:
            return self.intelligence
        if number == 6:
            return self.web
        if number == 7:
            return self.artifice
        if number == 8:
            return self.hp
        if number == 9:
            return self.ap
        if number == 10:
            return self.speed
        if number == 14:
            return self.lvl
        raise u"Statystyka nie obsługiwana przez metodę"

    def get_updated_statistic(self, number):
        """Metoda zwracająca wartość statystyki o danym numerze z ulepszeniami wynikającymi z wszelkich efektów na nią
        oddziałujących. UWAGA: metoda niekompletna - uwzględnia efekty pochodzące jedynie od talentów"""
        if number > 10: raise u'Statystyka nieobsługiwana.'
        tes = set() #Zbiór wszystkich efektów addytywnych wpływajacych na daną statystykę,
        # pobrana ze wszystkich talentów bohatera
        tem = set() #Zbiór wszystkich efektów multiplikatywnych wpływajacych na daną statystykę,
        # pobrana ze wszystkich talentów bohatera
        s = 0
        m = 100
        talents = self.talents.all()

        for t in talents:
            tes.add(t.effects.filter(where_works=number).filter(variable=number).filter(percent=False))
        for t in talents:
            tes.add(t.effects.filter(where_works=number).filter(variable=number).filter(percent=True))

        for effects_set in tes:
            for e in effects_set:
                s += e.value

        for effects_set in tem:
            for e in effects_set:
                m += e.value

        stat = self.get_statistic(number)
        if stat:
            up_stats = 0.01 * m * (stat + s)
            if up_stats < 1:
                return 1
            else:
                return up_stats
        else:
            return stat

    def get_updated_power(self):
        """Metoda zwracająca wartość mocy bohatera z ulepszeniami wynikającymi z wszelkich efektów na nią
        oddziałujących."""
        return self.get_updated_statistic(1)

    def get_updated_resistance(self):
        """Metoda zwracająca wartość wytrzymałości bohatera z ulepszeniami wynikającymi z wszelkich efektów na nią
        oddziałujących."""
        return self.get_updated_statistic(2)

    def get_updated_dexterity(self):
        """Metoda zwracająca wartość sprawności bohatera z ulepszeniami wynikającymi z wszelkich efektów na nią
        oddziałujących."""
        return self.get_updated_statistic(3)

    def get_updated_perception(self):
        """Metoda zwracająca wartość percepcji bohatera z ulepszeniami wynikającymi z wszelkich efektów na nią
        oddziałujących."""
        return self.get_updated_statistic(4)

    def get_updated_intelligence(self):
        """Metoda zwracająca wartość inteligencji bohatera z ulepszeniami wynikającymi z wszelkich efektów na nią
        oddziałujących."""
        return self.get_updated_statistic(5)

    def get_updated_web(self):
        """Metoda zwracająca wartość sieci bohatera z ulepszeniami wynikającymi z wszelkich efektów na nią
        oddziałujących."""
        return self.get_updated_statistic(6)

    def get_updated_artifice(self):
        """Metoda zwracająca wartość zaradności bohatera z ulepszeniami wynikającymi z wszelkich efektów na nią
        oddziałujących."""
        return self.get_updated_statistic(7)

    def get_updated_hp(self):
        """Metoda zwracająca ilość punktów życia bohatera z ulepszeniami wynikającymi z wszelkich efektów na nią
        oddziałujących."""
        return self.get_updated_statistic(8)

    def get_updated_ap(self):
        """Metoda zwracająca wartość punktów akcji bohatera z ulepszeniami wynikającymi z wszelkich efektów na nią
        oddziałujących."""
        return self.get_updated_statistic(9)

    def get_updated_speed(self):
        """Metoda zwracająca wartość szybkości bohatera z ulepszeniami wynikającymi z wszelkich efektów na nią
        oddziałujących."""
        return self.get_updated_statistic(10)

    def have_talent(self, talent):
        """Metoda sprawdzająca, czy bohater posiada dany talent"""
        return True if self.talents.filter(pk__contains=talent.pk) else False

    def have_required_stat(self, number, value):
        if number == 1:
            return self.power >= value
        if number == 2:
            return self.resistance >= value
        if number == 3:
            return self.dexterity >= value
        if number == 4:
            return self.perception >= value
        if number == 5:
            return self.intelligence >= value
        if number == 6:
            return self.web >= value
        if number == 7:
            return self.artifice >= value
        if number == 8:
            return self.hp >= value
        if number == 9:
            return self.ap >= value
        if number == 10:
            return self.speed >= value
        if number == 14:
            return self.lvl
        raise u"Statystyka nie obsługiwana przez metodę"

    def meets_stats_requirements(self, talent):
        pass

    def meets_talents_requiraments(self, talent):
        pass

    def meets_bloodline_requirament(self, talent):
        requirement = talent.blood_line_requirement
        return True if (not requirement) or self.blood_line == requirement else False

    def can_pick_talent(self, talent):
        """Metoda sprawdzająca, czy bohater może wybrać dany talent"""
        if self.meets_bloodline_requirament(talent):
            if self.meets_talents_requiraments(talent):
                if self.meets_stats_requirements(talent):
                    return True
        return False

    def __unicode__(self):
        return self.name