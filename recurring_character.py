
from sys import flags


def charString(strng):
    my_dict = {}
    global_flag = 0
    my_repeat = []
    for val in strng:
        print(val)

        if val in my_dict:
            my_repeat.append(val)
            global_flag = 1
            print(f'found repeat {val}')
        else:
            my_dict[val] = 1
    return my_repeat,global_flag


my_repeat,flag = charString("ABCDDYK")

if flag != 0:
    print(f'Letters that are repeated: {my_repeat}')