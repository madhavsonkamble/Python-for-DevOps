## To see the current directory 

"""import os
print(os.getcwd())"""

## OS library link: https://docs.python.org/3/library/os.html

## script to see disk usage
import shutil 

"""print(shutil.disk_usage("/"))"""

total, used, free = shutil.disk_usage("/")
print("Total disk sapce is:", total // (2**30)) 
print("used disk space is:", used // (2**30))
print("free disk space is:", free // (2**30))

## If want GB word should write in output
## Use formatted string or fstring

print(f"Total disk sapce is: {total // (2**30)} GB") 
print(f"used disk space is: {used // (2**30)} GB")
print(f"free disk space is: {free // (2**30)} GB")