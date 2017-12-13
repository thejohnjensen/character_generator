"""."""
import random


class CreateChar(object):
    """."""

    def __init__(self, name, role):
        """."""
        self.name = name
        self.role = role
        self.strength = 0
        self.dexterity = 0
        self.stamina = 0
        self.intelligence = 0
        self.armor = ''
        self.weapon = ''
        self.off_hand = ''


    def assign_attrs(self):
        """."""
        if self.role == 'warrior':
            self.strength = random.randint(30, 40)
            self.dexterity = random.randint(10, 20)
            self.stamina = random.randint(25, 35)
            self.intelligence = random.randint(5, 10)
        if self.role == 'mage':
            self.strength = random.randint(10, 15)
            self.dexterity = random.randint(10, 20)
            self.stamina = random.randint(15, 25)
            self.intelligence = random.randint(40, 50)
        if self.role == 'ranger':
            self.strength = random.randint(20, 25)
            self.dexterity = random.randint(35, 45)
            self.stamina = random.randint(25, 35)
            self.intelligence = random.randint(15, 25)


    def assign_equipment(self):
        """."""
        warrior_weapons = ['sword', 'axe', 'rubber chicken']
        warrior_armor = ['plate', 'mithril', 'kilt']
        warrior_off_hand = ['shield', 'sword', 'kitten']

        mage_weapons = ['wand', 'magic staff', 'pedantic come backs']
        mage_armor = ['robe', 'pointy hat', 'beard attachment']
        mage_off_hand = ['spell book', 'orb', 'broom']

        ranger_weapons = ['bow', 'staff', 'wolf']
        ranger_armor = ['leather', 'loin cloth', 'single eagle feather']
        ranger_off_hand = ['quiver', 'bear whistle', 'lantern']

        if self.role == 'warrior':
            self.armor = warrior_armor[random.randint(0, len(warrior_armor) - 1)]
            self.weapon = warrior_weapons[random.randint(0, len(warrior_weapons) - 1)]
            self.off_hand = warrior_off_hand[random.randint(0, len(warrior_off_hand) - 1)]
        if self.role == 'mage':
            self.armor = mage_armor[random.randint(0, len(mage_armor) - 1)]
            self.weapon = mage_weapons[random.randint(0, len(mage_weapons) - 1)]
            self.off_hand = mage_off_hand[random.randint(0, len(mage_off_hand) - 1)]
        if self.role == 'ranger':
            self.armor = ranger_armor[random.randint(0, len(ranger_armor) - 1)]
            self.weapon = ranger_weapons[random.randint(0, len(ranger_weapons) - 1)]
            self.off_hand = ranger_off_hand[random.randint(0, len(ranger_off_hand) - 1)]


if __name__ == '__main__':
    name = input('Please input your characters name: ')
    role = input('Please input a role; warrior, mage, ranger: ').lower()
    print(role)
    while role != 'warrior' and role != 'mage' and role != 'ranger':
        print('I\'m sorry please input either mage, warrior, or ranger for your role.')
        role = input('Please input a role; warrior, mage, ranger: ').lower()
    char = CreateChar(name, role)
    role = char.role
    char.assign_equipment()
    char.assign_attrs()
    armor = char.armor
    weapon = char.weapon
    off_hand = char.off_hand
    print('Congratulations! Your journey as a {} is about to begin.\
            Use your {} to keep you safe from harm, {} to do harm to others if you so choose,\
            and your {} to do whatever the hell you want with. Good Luck.'.format(role, armor, weapon, off_hand))