import roshambo


def test_translate():
    assert(roshambo.translate("A") == "rock")
    assert(roshambo.translate("X") == "rock")
    assert(roshambo.translate("B") == "paper")
    assert(roshambo.translate("Y") == "paper")
    assert(roshambo.translate("C") == "scissors")
    assert(roshambo.translate("Z") == "scissors")


def test_match():
    assert(roshambo.match("", "") == 0)
    assert(roshambo.match("A", "Y") == 8)
    assert(roshambo.match("B", "X") == 1)
    assert(roshambo.match("C", "Z") == 6)
    assert(roshambo.match("A", "X") == 4)
    assert(roshambo.match("A", "Y") == 8)
    assert(roshambo.match("B", "X") == 1)
    assert(roshambo.match("B", "Y") == 5)
    assert(roshambo.match("B", "Z") == 9)
    assert(roshambo.match("C", "X") == 7)
    assert(roshambo.match("C", "Y") == 2)
    assert(roshambo.match("C", "Z") == 6)


def test_run_strat():
    f = open("sample_input.txt", "r")
    assert(roshambo.run_strat(f) == 12)

