# Implement your function below.
def most_frequent(given_list):
    max_item = None
    my_dict = {}
    init_val = 0
    max_count = 0
    for x in given_list:
        if x in my_dict:
            
            my_dict[x] = my_dict[x] +1

        else:
            init_val = 1
            my_dict[x] = 1

        if my_dict[x] > max_count:
            max_count = my_dict[x]
            max_item = x
    
    return max_item,max_count

# NOTE: The following input values will be used for testing your solution.
# most_frequent(list1) should return 1
list1 = [1, 3, 1, 3, 2, 1]
# most_frequent(list2) should return 3
list2 = [3, 3, 1, 3, 2, 1]
# most_frequent(list3) should return None
list3 = []
# most_frequent(list4) should return 0
list4 = [0]
# most_frequent(list5) should return -1
list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]


i,c = most_frequent(list5)

print (f' max item = {i} , max count = {c}' )