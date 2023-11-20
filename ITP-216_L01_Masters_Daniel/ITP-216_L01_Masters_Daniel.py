#ITP 216 Lab 2
# Name: Daniel Masters
# Email: damaster@usc.edu

def main():
    user_input = input("Please enter an input to be converted: ")    #get user input

    print("string: ", end="")     #print statement before the users input as a string
    for i in user_input:          #for loop to iterate over user input
        print(i, end=", ")
    print()

    user_list = list(user_input)
    print("list: ", end="")     #print statement before the users input as a list
    for i in user_list:          #for loop to iterate over user input in list
        print(i, end=", ")
    print()                     #spacing

    user_dict = {}                  #declaring dictionary
    user_tuple = tuple(user_input)  #declare user input as a tuple
    print("tuple: ", end="")
    for i in user_tuple:        #for loop to iterate over user input in tuple
        print(i, end=", ")
        user_dict[i] = user_dict.get(i, 0) + 1      #sets each letter as key in dictionary as zero, add one, tracks
    print()                                         #each letter


    user_set = set(user_input)          #declaring each set
    print("set: ", end="")
    for i in user_set:          #for loop to iterate over user input in set
        print(i, end=", ")
    print()

    print("dictionary: ", end="\n")     #printing the dictionary
    for i, j in user_dict.items():      #prints each item in the dictionary
        print(f"\t{i}: {j}")

if __name__ == '__main__':
    main()
