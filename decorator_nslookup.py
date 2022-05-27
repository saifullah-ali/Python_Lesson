import re
import os
import subprocess
class netConnect(object):
    def __init__ (self):
        ping = os.popen('ping -c 4 google.com')
        ping = ping.read()
        print(ping)
        check = re.search("0.0% packet loss",ping)
        if check:
            print(f' found {check.group()} --> ping passed')
        else:
            print("sanity check failed")
    def find_dns(self,webname):
        self.webname = webname
        lookup = os.popen('nslookup self.webname')
        print(lookup.read())
        lookup = subprocess.run(['nslookup',self.webname],stdout = subprocess.PIPE, universal_newlines = True)
        print(lookup.stdout)
        add = re.findall("Address: (\d+.\d+.\d+.\d+)",lookup.stdout)
        if add:
            print(add)



#d = netConnect()
#d.find_dns("twitter.com")

my_list = [1,2,3,4,5,6,7,8]
fast = 0
slow = 0

for i in range(len(my_list)):
    slow = slow +1
    fast = fast +2
    if fast > len(my_list):
        break
    print(f'slow {slow} is {my_list[slow]} and fast index {fast}')
slow = slow -1
rev_list = []
for i in range(slow,len(my_list)):
    print(i)
    rev_list.append(my_list[i])

print(rev_list[::-1])

def my_sum(**args):
    result = 0
    for x in args.values():
        result += x
    return result

print(my_sum(a = 1,b = 2,d = 3))


##decorator::
#------------
def create_adder(x):
    def adder(y):
        return x+y
 
    return adder
 
add_15 = create_adder(15) ##add_15 will become adder
 
print(add_15(10))

#decorator example #2
def logged(func):
    def with_logging(*args):
        print(func.__name__ + " was called")
        print(*args)
        return func(2)
    return with_logging

@logged ##option 2
def f(x):
    print("inside f(x)")
    print(x)
    return x + x * x
#f = logged(f)#here f became 'with logging' --> option 1
print(f(8))



