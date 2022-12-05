
rows = []
for stack in range(1, 12):
    rows.append([])


def move_crates(number_to_move, source, dest):
    containers = []
    for moves in range(0, number_to_move):
        containers.append(rows[int(source)].pop())
    containers.reverse()
    print(f"Move {number_to_move} ({containers}) from {source} to {dest}")
    for container in containers:
        rows[dest].append(container)


f = open("input.txt", "r")
for stack in range(1, 9):
    row = f.readline()
    print(f"{row[1:2]}\t{row[5:6]}\t{row[9:10]}\t{row[13:14]}\t{row[17:18]}\t{row[21:22]}\t{row[25:26]}\t{row[29:30]}\t{row[33:34]}")
    rows[1].append(row[1:2])
    rows[2].append(row[5:6])
    rows[3].append(row[9:10])
    rows[4].append(row[13:14])
    rows[5].append(row[17:18])
    rows[6].append(row[21:22])
    rows[7].append(row[25:26])
    rows[8].append(row[29:30])
    rows[9].append(row[33:34])

for row in range(1, 10):
    rows[row].reverse()
    rows[row] = ([i for i in rows[row] if i != " "])

for line in f:
    if "move" in line:
        number_to_move = int(line.split(" ")[1])
        source = int(line.split(" ")[3])
        dest = int(line.split(" ")[5])
        print(f"{source} :: PRE :: {rows[source]}")
        print(f"{dest} :: PRE :: {rows[dest]}")
        move_crates(number_to_move, int(source), int(dest))
        print(f"{source} :: POST :: {rows[source]}")
        print(f"{dest} :: POST :: {rows[dest]}\n\n")

for row in range(0, len(rows)):
    print(rows[row][-1:])
