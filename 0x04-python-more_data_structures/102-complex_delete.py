#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    del_list = []
    for key, val in a_dictionary.items():
        if val == value:
            del_list.append(key)
    for each in del_list:
        del a_dictionary[each]

    return a_dictionary
