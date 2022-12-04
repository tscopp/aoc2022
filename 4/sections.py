def range_to_list(element):
    range_list = []
    for item in range(int(element.split("-")[0]), int(element.split("-")[1]) + 1):
        range_list.append(item)
    return range_list


def is_contained(set1, set2):
    if(all(x in set1 for x in set2) or all(x in set2 for x in set1)):
        return True
    return False


f = open("input.txt", "r")
contained_pairs = 0
for line in f:
    set1 = range_to_list(line.split(",")[0])
    set2 = range_to_list(line.split(",")[1])
    if is_contained(set1, set2):
        contained_pairs = contained_pairs + 1

print(contained_pairs)
