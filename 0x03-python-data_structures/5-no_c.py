#!/usr/bin/python3
def no_c(my_string):
    new_string = ''
    for str in range(len(my_string)):
        if my_string[str] == 'c' or my_string[str] == 'C':
            continue
        new_string += my_string[str]

    return new_string
