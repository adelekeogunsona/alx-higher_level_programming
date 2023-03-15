#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    average = 0

    for my_tuple in my_list:
        score = my_tuple[0]
        weight = my_tuple[1]
        sum += score * weight
        average += weight

    return sum/average
