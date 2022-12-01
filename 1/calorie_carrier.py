f = open("input.txt", "r")
elf_counter = 0
elf_calories = 0
biggest_carry = 0
for line in f:
    if len(line) == 1:
        if elf_calories > biggest_carry:
            biggest_carry = elf_calories
        elf_counter = elf_counter + 1
        elf_calories = 0
    else:
        elf_calories = elf_calories + int(line)
print(biggest_carry)
