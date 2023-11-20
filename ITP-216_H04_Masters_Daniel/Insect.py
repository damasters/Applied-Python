import random
from Arthropod import Arthropod
#import arthropod bc insect is a child of it
class Insect(Arthropod):
    #class attribute
    insect_count = 0
    #using the params from arthropod and adding wings count
    #increase insect count by one
    def __init__(self, name_param, color_param, limbs_count_param, wings_count_param):
        super().__init__(name_param, color_param, limbs_count_param)
        self.wings_count = wings_count_param
        Insect.insect_count += 1
    #string method returns string of how many limbs and wings insect has
    def __str__(self):
        return 'The ' + self.color + ' ' + self.name + ' has ' + str(self.limbs) + \
               ' limbs and ' + str(self.wings_count) + ' wings.'
    #getter that returns number of wings
    def get_wings_count(self):
        return self.wings_count
    #getter that returns power level
    def get_power(self):
        return self.limbs + self.wings_count
    #method for losing fight, adds onto the lose fight method from arthropod: includes losing wings
    def lose_fight(self):
        super().lose_fight()
        #only subtracts when greater than zero, prevents range error
        if self.wings_count > 0:
            wings_to_lose = random.randint(1, self.wings_count)
            self.wings_count -= wings_to_lose

filter_list = [ i in veggies]