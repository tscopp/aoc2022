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
sacks = []
for line in f:
    sacks.append(line)
for sack in range(0, len(sacks), 3):
    c1 = sacks[sack]
    c2 = sacks[sack + 1]
    c3 = sacks[sack + 2]

    intersections.append(list(set(c1.strip()).intersection(set(c2.strip())).intersection(set(c3.strip()))))

total_priority = 0
for i in intersections:
    total_priority = total_priority + priority[i[0]]
print(total_priority)
