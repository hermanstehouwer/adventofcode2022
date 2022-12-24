from lib.read.lists import file_to_list
from lib.types.blizzard import Blizzard


def test_small_blizzards():
    iter = file_to_list("tests/data/day24_small.txt")
    blizzard = Blizzard(iter)
    for t in blizzard.death.keys():
        print(f"at time {t} death comes at positions {blizzard.death[t]}")
    assert (2,2) in blizzard.death[1]


def test_part1():
    iter = file_to_list("tests/data/day24.txt")
    blizzard = Blizzard(iter)
    assert blizzard.lenght_fastest_path() == 18


def test_part2():
    iter = file_to_list("tests/data/day24.txt")
    blizzard = Blizzard(iter)
    assert blizzard.lenght_fastest_path(forgot_snacks=True) == 54
