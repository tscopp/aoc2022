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
        char_list.append(input_list[char_counter + 4])
        char_list.append(input_list[char_counter + 5])
        char_list.append(input_list[char_counter + 6])
        char_list.append(input_list[char_counter + 7])
        char_list.append(input_list[char_counter + 8])
        char_list.append(input_list[char_counter + 9])
        char_list.append(input_list[char_counter + 10])
        char_list.append(input_list[char_counter + 11])
        char_list.append(input_list[char_counter + 12])
        char_list.append(input_list[char_counter + 13])
        if len(set(char_list)) == len(char_list):
            print(f"Unique: {char_list}")
            char_counter += 14
            break
        else:
            print(f"Not Unique: {char_list}")

    except IndexError as e:
        print(e)
    print("\n")
    char_counter += 1

print(char_counter)


