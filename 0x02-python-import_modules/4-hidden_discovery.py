#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    all = dir(hidden_4)
    for each in all:
        if each[0:2] != "__":
            print(each)
