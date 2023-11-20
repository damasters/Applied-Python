#import arachnid and insect classes
from Arachnid import Arachnid
from Insect import Insect

def main():
    #create variables of objects based on classes
    insect1 = Insect('mosquito', 'silver', 6, 2)
    arach1 = Arachnid('wolf spider', 'gray', 8, False)
    #print statements from directions
    print("Your contenders:")
    print("\t"+str(insect1))
    print("\t"+str(arach1))
    print()
    #loop while the bugs have limbs/wings
    round_count = 1
    loop = True
    while (insect1.get_wings_count() > 0 or insect1.get_limbs_count() > 0) and arach1.get_limbs_count() > 0 and loop == True:
        #determine the winner of the round based on power
        insect_power = insect1.get_power()
        arach_power = arach1.get_power()
        #if the power level of a bug or arachnid is greater, pick them as winner
        if insect_power > arach_power:
            arach1.lose_fight()
            print('Round ' + str(round_count) + ': ', end='')
            print('The ' + insect1.get_name() + ' wins this round!')
            print('\t', arach1)
        #else they lose the fight
        else:
            insect1.lose_fight()
            print('Round ' + str(round_count) + ': ', end='')
            print('The ' + arach1.get_name() + ' wins this round!')
            print('\t', insect1)
        #if the insect loses all its wings and limbs or an arachnid loses all its limbs, the fight is over
        if (insect1.get_limbs_count() == 0 and insect1.get_wings_count() == 0) or arach1.get_limbs_count() == 0:
            #a winner is declared
            print('There is a winner!')
            if insect1.get_limbs_count() == 0 and insect1.get_wings_count() == 0:
                print('\t', arach1)
            else:
                print('\t', insect1)
            #break out of the while loop
            loop = False
        #increase the round count
        round_count += 1

if __name__ == '__main__':
    main()
