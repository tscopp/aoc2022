from string import ascii_lowercase as alc

f = open("input.txt", "r")

priority = {}

counter = 1
for a in alc:
    priority[a] = counter
    counter = counter + 1

for a in alc:
    priority[a.upper()] = counter
    counter = counter + 1

intersections = []
for line in f:
    midpoint = int(len(line) / 2)
    c1 = line[:midpoint]
    c2 = line[midpoint:]
    intersections.append(list(set(c1).intersection(set(c2))))

total_priority = 0
for i in intersections:
    print(i)
    total_priority = total_priority + priority[i[0]]
print(total_priority)
