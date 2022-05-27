# Implement your function below.
def non_repeating(given_string):
    my_list = []
    val =0
    my_dict = {}
    length = len(given_string)
    for x in given_string:
        if x in my_dict:
            my_dict[x] = my_dict[x] + 1
        else:
            my_dict[x] = 1


    for x in given_string:
        if my_dict[x] < 2:
            return x
    
    
    return None

# NOTE: The following input values will be used for testing your solution.
non_repeating("abcab") # should return 'c'
non_repeating("abab") # should return None
res = non_repeating("aabbbc") # should return 'c'
non_repeating("aabbdbc") # should return 'd'

print(f'result is {res}')