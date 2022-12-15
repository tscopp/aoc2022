from collections import defaultdict
import os

input_data = open("sample_input.txt", "r")
history = input_data.read()[2:].split("\n$ ")
pwd = []
sizes = defaultdict(int)
children = defaultdict(list)
for element in history:
    command = element[:2]
    if command == "ls":
        contents = element.split("\n")[1:]
        directory_size = 0
        for item in contents:
            if item.split(" ")[0] == "dir":
                dir_name = item.split(" ")[1]
                print(f"Found Child: {os.path.join(*pwd, dir_name)}")
                children[os.path.join(*pwd)].append(dir_name)
                print("Directory") 
                
            else:
                print(item)
                size, name = item.split(" ")
                print(f"{size} -- {name}")
                directory_size += int(size)
                abspath = os.path.join(*pwd)
                sizes[abspath] = directory_size     # without subs 
        print(directory_size)
        print(contents)
    if command == "cd":
        print(f"Old PWD: {pwd}")
        destination = element.split(" ")[1]
        print(f"Change Directory {destination}")
        if destination == "..":
            pwd.pop()
        else:
            pwd.append(destination)
        print(f"New PWD: {pwd}")
print(sizes)
for key in sizes:
    if len(key.split("/")) > 2:
        path = key.split("/")
        for i in path:
            print(os.path.join("/", *path))
            subdir_size = sizes[os.path.join("/", *path)]
            path.pop()
            parent_size = sizes[os.path.join("/", *path)]
            if subdir_size != parent_size:
                sizes[os.path.join("/", *path)] += subdir_size
                
print(sizes)    

solution = 0
for i in sizes:
    if int(sizes[i]) <= 100000:
        solution += sizes[i]
        print(i)
print(solution)