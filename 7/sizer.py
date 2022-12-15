from collections import namedtuple
from os import path

File = namedtuple('file', ['name', 'size'])
root = []
pwd = []
directories = {}

def ls():   # list out the entire tree
    pass

def is_command(logline):
    return bool([*logline][0] == "$")

f = open("sample_input.txt", "r")
for line in f:
    change_path = ""
    if is_command(line):
        print(line.strip("\n").split(" "))
        command = line.strip("\n").split(" ")
        if command[1] == "cd":
            print("change_dir")
            print(command[2])
            if command[2] == "/":
                pwd = ["/"]
                print("reset pwd")
            elif command[2] == "..":
                print(pwd)
                pwd.pop()
                print(pwd)
            else:
                change_path = command[2]
                directories[change_path] = []
                pwd.append(change_path)
                print(pwd)
                

            
    else:
        print(f"!{pwd}/{line}")
        if line.split(" ")[0] == "dir":
            dir_name = pwd[-1]
            print(dir_name)
            directories[dir_name] = []
            print(f"Discovered dir {dir_name}")
        else:
            directories[pwd[-1]] = []
            size = line.split()[0]
            name = line.split()[1]
            print(f"!{size}{name}")
            print(line)
            print(pwd)
            print(len(pwd))
            for i in range(0,len(pwd)):
                directories[pwd[-1]].append(File(name, size))
            print(directories)
        print(directories)