from asyncio import subprocess
import subprocess
import os
import re
#https://janakiev.com/blog/python-shell-commands/
#Using system commands
cmd ="date"

output = os.popen('ls -ltr /Users/s.b.ali/Downloads/GitRepository/python_discrete_dev/')
print(f'first output popen of ls -ltr \n {output.read()}')

output = os.popen('pwd')
print(f'second output popen - pwd \n {output.read()}')

process = subprocess.run(['pwd'], 
                         stdout=subprocess.PIPE, 
                         universal_newlines=True)


print(f'output of subprocess run - \n {process.stdout}')

process = subprocess.run(['ls','-l','/Users/s.b.ali/Downloads/GitRepository/python_discrete_dev'], 
                         stdout=subprocess.PIPE, 
                         universal_newlines=True)


print(f'output of detailed subprocess run ls -la \n {process.stdout}')

#for i in process.stdout:
#    print(i)
#    print("ok")

lines = process.stdout.splitlines()
ndict={}
for i in lines:
    print(f'lines printing {i}')
    m = re.search('(\D+$|\D+\.\D+$)',i)
    if m:
        print(m.group())
        n = re.search('(\d+)(.*?)(\d+)',i)
        if n.group(3):
            print(n.group(3))
            #ndict[n.group(3)] = m.group()
            ndict[m.group()] = n.group(3)

print(ndict)
size = 0
file=''
for x in ndict:
    if int(ndict[x]) > size:
        size = int(ndict[x])
        file = x
        file = file.replace(" ","")


print(f'largest file is {file} with size of {size}')


cur_loc = "/Users/s.b.ali/Downloads/GitRepository/python_discrete_dev"
cur_loc = cur_loc+"/"+file
print(cur_loc)


f1 = open(cur_loc,"r")

f2 = open("newfile","w")

for lines1 in f1:
    f2.write(lines1)

f1.close()
f2.close()


