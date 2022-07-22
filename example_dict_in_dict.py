class Heroes():
    """Class of great Heroes"""
    def __init__(self, name, level, race):
        """Initiate Heroes"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        """Print all parameters"""
        discription = (self.name + " Level is: " + str(self.level) + ", Race is: " + self.race + ", Health is: " + str(self.health)).title()
        print(discription)

    def level_up(self):
        """Upgrade Level of Hero"""
        self.level += 1
        print(self.name + " Get Level Up")

    def move(self):
        """Hero move"""
        print("Hero " + self.name + " start moving...")



myhero1 = Heroes('Andrey_Bogatur', 11, 'asian')
myhero2 = Heroes('Vityaz_Dima', 10, 'russian')
myhero3 = Heroes('Dunidze_Zag_Zag', 13, 'orc')
myhero4 = Heroes('Ivan_Huevich', 12, 'ingener')
myhero5 = Heroes('Danila_Korolevich', 15, 'heal_master_elf')

myhero1.show_hero();
myhero5.move()
myhero2.level_up()
myhero2.show_hero()
myhero3.move()
myhero4.level_up()
myhero4.show_hero()