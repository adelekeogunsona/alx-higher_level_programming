#!/usr/bin/python3
def best_score(a_dictionary):

    if a_dictionary:
        largest = 0
        for key, value in a_dictionary.items():
            if a_dictionary[key] > largest:
                largest = a_dictionary[key]
                name = key
        return name
    else:
        return None
