# Name: Daniel Masters
# Spring 2022
# Section: 31883
# ITP 216 Homework 02

def main():
    cats_names = ('Cassandra', 'Sir Whiskington', 'Truck')
    dogs_names = {'Barkey McBarkface', 'Leeloo Dallas', 'Taro'}
    parrots_names = ['Squawk', 'Squawk 2: the Squawkquel', 'Larry']
    names = ['peter', 'paul', 'mary']
    animals = ('cat', 'cat', 'hamster') #list copied from directions
    user_choice = 0  #declared user's choice for loop program options
    user_dict = {}   #dictionary for all lists
    bool_continue = True   #boolean for when user wants to exit program
    user_dict["cat"] = list(cats_names)  #making types the key and names the values
    user_dict["dog"] = list(dogs_names)
    user_dict["parrot"] = list(parrots_names)
    for i in range(3):  #for loop for  animal types with the animal names if not in dict, make new key and append values
        if animals[i] in user_dict.keys():
            user_dict[animals[i]].append(names[i].title())
        else:
            user_dict[animals[i]]=[]
            user_dict[animals[i]].append(names[i].title())
    username = input("Please enter your name: ")    #have user input their name
    print("Hi,", username + "!")    #say hi to user
    while bool_continue == True:    #if user does not type the 3rd option keep looping
        print("Please choose from the following options:")  #menu of options
        print("\t 1. See all your pets' names.")
        print("\t 2. Add a pet.")
        print("\t 3. Exit")
        while user_choice < 1 or user_choice > 3:   #if the user choice is not one of the options keep looping
            user_input = input("What would you like to do? (1, 2, 3): ")
            print() #spacing
            try:    #tries to put user value as an int, if that does not work print that it is not a number, continue loop
                user_choice = int(user_input)
                if user_choice < 1 or int(user_input) > 3:  #if the value does not fall in between 1 and 3, continue loop
                    print("That number is not valid.")
            except ValueError:
                print("That is not a number.")
        if user_choice == 1: #if user types one
            num_pets = 0
            for i in user_dict.keys():  #loop through keys and print the amount of values as the number of pets
                num_pets = num_pets + len(user_dict[i])
            print("You have "+str(num_pets)+" pets.")
            for i in user_dict.keys():  #print the pets and their names
                print(i+": ", end="")
                print(", ".join(user_dict[i]))
            user_choice = 0 #sends back to beginning of loop
            print()
        elif user_choice == 2:  #if user selects second option
            sec_input = input("What kind of animal is this?: ")
            print()
            animal_name = input("What is the name of the "+sec_input+"?: ")
            print()
            if sec_input in user_dict.keys():   #searches for the users input in the existing keys
                user_dict[sec_input].append(animal_name.title())
            else:   #if does not find it in existing keys makes new one and attaches value to it
                user_dict[sec_input] = []
                user_dict[sec_input].append(animal_name.title())
            print("Great! "+animal_name.title()+" the "+sec_input+" is now added to your pets.")
            print()
            user_choice = 0
        else:   #if user types 3, bool is false, loop breaks and goodbye is printed
            bool_continue = False
    print("Goodbye!")

if __name__ == '__main__':
    main()
