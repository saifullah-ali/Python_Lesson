# Implement your function below.
def is_rotation(list1, list2):
    final_loc = -1
    if len(list1) != len(list2):
        return False
    loc_a = 0
    loc_b = 0
    for loc_b in range(0,len(list2)-1):
        if list2[loc_b] == list1[0]:
            print(f'found match at {loc_b} of array B')
            final_loc = loc_b
            break
    if final_loc == -1:
        return False
    print(f'final location: {final_loc}')
    for loc_a in range(0, len(list1)-1):
        if list1[loc_a] != list2[final_loc]:
            print(f"abc {list1[loc_a]} and {list2[final_loc]}")
            return False
        else:
            print("passed")
            if final_loc == len(list2)-1:
                final_loc =0
                        #loc_a = loc_a+1
            else:
                final_loc = final_loc +1

    return True



# NOTE: The following input values will be used for testing your solution.
list1 = [1, 2, 3, 4, 5, 6, 7]
list2a = [4, 5, 6, 7, 8, 1, 2, 3]
# is_rotation(list1, list2a) should return False.
list2b = [4, 5, 6, 7, 1, 2, 3]
# is_rotation(list1, list2b) should return True.
list2c = [4, 5, 6, 9, 1, 2, 3]
# is_rotation(list1, list2c) should return False.
list2d = [4, 6, 5, 7, 1, 2, 3]
# is_rotation(list1, list2d) should return False.
list2e = [4, 5, 6, 7, 0, 2, 3]
# is_rotation(list1, list2e) should return False.
list2f = [1, 2, 3, 4, 5, 6, 7]
# is_rotation(list1, list2f) should return True.
list2g = [7, 1, 2, 3, 4, 5, 6]
# is_rotation(list1, list2g) should return True.

print(is_rotation(list1,list2g))