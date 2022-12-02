f = open("input.txt", "r")
elf_counter, elf_calories, top3_carry = 0, 0, 0
elf_carry = []

for line in f:
    if len(line) == 1:
        elf_carry.append(int(elf_calories))
        elf_counter = elf_counter + 1
        elf_calories = 0
    else:
        elf_calories = elf_calories + int(line)

for carry in sorted(elf_carry)[-3:]:
    top3_carry = top3_carry + carry

print(top3_carry)
