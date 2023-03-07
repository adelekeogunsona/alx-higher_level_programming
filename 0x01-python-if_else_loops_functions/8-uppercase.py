#!/usr/bin/python3
def uppercase(str):
    for string in str:
        string = ord(string)
        if string in range(97, 123):
            string -= 32
        print("{}".format(chr(string)), end='')
    print()
