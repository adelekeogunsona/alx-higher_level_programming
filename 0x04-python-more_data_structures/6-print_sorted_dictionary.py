#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    my_list = []

    for key in a_dictionary:
        my_list.append(key)

    for i in range(len(my_list)):
        new_list = sorted(my_list)
        key = new_list[i]
        value = a_dictionary[new_list[i]]
        print("{}: {}".format(key, value))
