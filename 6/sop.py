f = open("input.txt", "r")

for line in f:
    input_list = [*line]

char_counter = 0
for character in input_list:
    char_list = []
    try:
        char_list.append(input_list[char_counter])
        char_list.append(input_list[char_counter + 1])
        char_list.append(input_list[char_counter + 2])
        char_list.append(input_list[char_counter + 3])
        if len(set(char_list)) == len(char_list):
            print(f"Unique: {char_list}")
            char_counter += 4
            break
        else:
            print(f"Not Unique: {char_list}")

    except IndexError as e:
        print(e)
    print("\n")
    char_counter += 1

print(char_counter)


