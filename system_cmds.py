from asyncio import subprocess
import subprocess
import os
#https://janakiev.com/blog/python-shell-commands/
#Using system commands
cmd ="date"
#returned = subprocess.check_output(cmd)

#print(returned.decode("utf-8"))


#os.system("ls -ltr")

output = os.popen('ls -ltr')
print(f'first output popen - ls -ltr \n {output.read()}')

output = os.popen('pwd')
print(f'second output popen - pwd \n {output.read()}')

process = subprocess.run(['pwd'], 
                         stdout=subprocess.PIPE, 
                         universal_newlines=True)


print(f'output of subprocess run - \n {process.stdout}')

process = subprocess.run(['ls','-la','/Users/s.b.ali/Downloads/GitRepository/python_discrete_dev'], 
                         stdout=subprocess.PIPE, 
                         universal_newlines=True)


print(f'output of detailed subprocess run ls -la \n {process.stdout}')

