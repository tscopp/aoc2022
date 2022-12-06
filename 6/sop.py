f = open("input.txt", "r")

for line in f:
    input_list = [*line]

char_counter = 0
for character in input_list:
    char_list = []
    for i in range(0, 4):
        try:
            char_list.append(input_list[char_counter + i])
        except IndexError as e:
            print(e)
    if len(set(char_list)) == len(char_list):
        print(f"Unique: {char_list}")
        char_counter += len(char_list)
        break
    else:
        print(f"Not Unique: {char_list}")

    print("\n")
    char_counter += 1

print(char_counter)


