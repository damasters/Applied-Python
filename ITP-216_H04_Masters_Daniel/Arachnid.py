from Arthropod import Arthropod
#import arthropod bc arachnid is a child of it
class Arachnid(Arthropod):
    arachnid_count = 0  #class attribute
    # self refers to the instance you just created
    # super class to designate the classes inherited from arthropod
    def __init__(self, name_param, color_param, limbs_count_param, venomous_param):
        super().__init__(name_param, color_param, limbs_count_param)
        self.venomous = venomous_param
        Arachnid.arachnid_count += 1               #increase count by 1

    #the creating string method for if the arachnid is venomous or not, returns string
    def __str__(self):
        if self.venomous:
            is_venomous = "venomous"
        else:
            is_venomous = "non-venomous"
        return 'The ' + self.color + ' ' + is_venomous + ' ' + self.name + ' has ' \
               + str(self.limbs) + ' limbs.'
    #getter for whether or not arachnid is venomous
    def get_venomous(self):
        return self.venomous
    #getter for getting the power level of arachnid
    def get_power(self):
        if self.venomous:
            return self.limbs*2
        else:
            return self.limbs









