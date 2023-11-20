# ITP-216 Lab 04
# Daniel Masters
# Email: damaster@usc.edu

# Class Arthropod
import random


class Arthropod(object):
    # Class Attributes
    arthropod_count = 0
    # 1. arthropod_count

    # a. The number of arthropods created.
    # Instance Attributes
    # 1. self.name
    # a. The name of the arthropod (string)
    # 2. self.limbs
    # a. The number of limbs the arthropod has (int)
    # 3. self.color
    # a. The color of the arthropod (String)

    # Instance Methods
    # 1. __init__()
    # a. Description: Constructs a new arthropod object
    # b. Parameters: 3
    # i. name_param (String)
    # ii. color_param (String)
    # iii. limbs_count_param (int)
    # c. Returns 0
    # d. Assigns parameters to instance attributes. Increases arthropod arthropod_count by 1.
    def __init__(self, name_param, color_param, limbs_count_param):
        # 1. self.name
        self.name = name_param  # a. The name of the arthropod (string)
        # 2. self.limbs
        self.limbs = limbs_count_param # a. The number of limbs the arthropod has (int)
        # 3. self.color
        self.color = color_param # a. The color of the arthropod (String)
    def __str__(self):
        return 'Arthropod named: ' + self.name + ' is color: ' + self.color + \
               ' and has ' + str(self.limbs) + ' limbs.'
    # 2. get_name()
    # a. Description: Retrieves arthropod name.
    # b. Parameters: 0
    # c. Returns: 1
    # i. self.name instance attribute
    def get_name(self):
        return self.name
    # 3. get_color()
    # a. Description: Retrieves arthropod color.
    # b. Parameters: 0
    # c. Returns: 1
    # i. self.color instance attribute
    def get_color(self):
        return self.color
    # 4. get_limbs_count()
    # a. Description: Retrieves arthropod limbs count.
    # b. Parameters: 0
    # c. Returns: 1
    # i. self.limbs_count instance attribute
    def get_limbs_count(self):
        return self.limbs
    # 5. set_color()
    # a. Description: Changes arthropod color.
    # b. Parameters: 1
    # i. A color (String)
    # c. Returns: 0
    def set_color(self, color_param):
        self.color = color_param

    # 6. lose_fight()
    # a. Description: arthropod potentially loses limbs.
    # b. Parameters: 0
    # c. Returns: 0
    # d. Based on the number of existing limbs, randomly generate a number and lose that number of
    # limbs. update self.limbs_count instance attribute.
    def lose_fight(self):
        # Based on the number of existing limbs, randomly generate a number and lose that number of
        limbs_to_lose = random.randint(1, self.limbs) #randint does up to and including the number
        self.limbs -= limbs_to_lose

def main():
    arthro1 = Arthropod('bug1', 'red', 6)   #tests our __innit__
    arthro2 = Arthropod('bug2', 'blue', 4)
    print("Before fight:")
    print(arthro1)                          #tests out __str__
    print(arthro2)
    arthro1.set_color('green')
    print(arthro1.get_color())
    arthro1.lose_fight()
    arthro2.lose_fight()
    print("After fight:")
    print(arthro1)
    print(arthro2)

if __name__ == '__main__':
    main()