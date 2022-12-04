import sections

f = open("sample_input.txt", "r")


def test_range_to_list():
    # for line in f:
    #    for element in line.split(","):
    #        print(element)
    assert(sections.range_to_list("2-4") == [2, 3, 4])
    assert(sections.range_to_list("6-8") == [6, 7, 8])
    assert(sections.range_to_list("2-3") == [2, 3])
    assert(sections.range_to_list("4-5") == [4, 5])
    assert(sections.range_to_list("5-7") == [5, 6, 7])
    assert(sections.range_to_list("7-9") == [7, 8, 9])
    assert(sections.range_to_list("2-8") == [2, 3, 4, 5, 6, 7, 8])
    assert(sections.range_to_list("3-7") == [3, 4, 5, 6, 7])
    assert(sections.range_to_list("6-6") == [6])
    assert(sections.range_to_list("4-6") == [4, 5, 6])
    assert(sections.range_to_list("2-6") == [2, 3, 4, 5, 6])
    assert(sections.range_to_list("4-8") == [4, 5, 6, 7, 8])


def test_is_contained():
    assert(sections.is_contained(sections.range_to_list("2-6"), sections.range_to_list("4-8")) is False)
    assert(sections.is_contained(sections.range_to_list("4-8"), sections.range_to_list("2-6")) is False)
    assert(sections.is_contained(sections.range_to_list("1-10"), sections.range_to_list("2-4")) is True)
    assert(sections.is_contained(sections.range_to_list("2-4"), sections.range_to_list("1-10")) is True)
    assert(sections.is_contained(sections.range_to_list("10-20"), sections.range_to_list("11-15")) is True)
    assert(sections.is_contained(sections.range_to_list("11-15"), sections.range_to_list("10-20")) is True)
