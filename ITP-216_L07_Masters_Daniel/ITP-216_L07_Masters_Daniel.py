# Name: Daniel Masters
# Spring 2022
# Section: 31883
# ITP 216 Lab 07

import functools

# 1. Write a decorator function validator_decorator which will validate the decorated function's input:
# a. All the decorated function's args should be strings.
# b. All the decorated function's kwargs values should be dictionaries with two key:value pairs.
# c. Display a message informing the user of whether or not the decorated function's arguments pass the test.
def validator_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Testing arguments: ')
        arg_types = [type(arg) for arg in args]  #map()
        arg_flags = [arg_type == str for arg_type in arg_types] #map()
        if False in arg_flags or len(kwargs) != 2:
            if False in arg_flags:
                print('\tArguments rejected: not all args are strings.')
            if len(kwargs) != 2:
                print('\tArguments rejected: not all kwargs have two key:value pairs')
        else:
            print('\tArguments accepted: all args are Strings, and all kwargs are dictionaries with two k:v pairs')

        print('Printing args:')
        for arg in args:
            print('\t', arg)
        print('Printing kwargs:')
        print('\t', 'animal:',kwargs)

        print('Running function: ', end='\n\n')
        func(*args, **kwargs)
    return wrapper

# 2. Write a function to be decorated called print_all_the_things() which prints out the args all on one line, and
# the kwargs' key:value pairs on separate, indented lines. You will use this to test your validator decorator.
# 3. Decorate the function from #2 with the decorator from #1.
@validator_decorator
def print_all_the_things(*args, **kwargs):
    print('This will print all the things:', end='\n\t')
    print(*args)
    for kwarg in kwargs:
        print('\t', kwarg, ': ', kwargs[kwarg], sep='')

def main():
    print_all_the_things('Another', 'lab', 'involving', 'animals.', cat = True, dog = False)
    print('-------------------------------------------------------------------------------')
    print_all_the_things('Never', 'Eat', 'Shredded', 'Wheat', cat=True, dog=False, hamster='never')

if __name__ == '__main__':
    main()
