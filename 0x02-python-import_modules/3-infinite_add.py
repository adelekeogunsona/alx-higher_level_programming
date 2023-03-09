#!/usr/bin/python3
import sys

if __name__ == "__main__":
    sum = 0
    length = len(sys.argv)

    for i in range(1, length):
        sum += int(sys.argv[i])

    print(sum)
