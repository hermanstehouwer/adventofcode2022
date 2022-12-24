from lib.read.lists import file_to_list
from lib.types.grove_planting import GrovePlanting


def test_small_part1():
    iter = file_to_list("tests/data/day23_small.txt")
    grove = GrovePlanting(iter)
    assert grove.count_empty_ground() == 3
    grove.rounds(10)
    assert grove.count_empty_ground() == 25


def test_part1():
    iter = file_to_list("tests/data/day23.txt")
    grove = GrovePlanting(iter)
    assert grove.count_empty_ground() == 27
    grove.rounds(10)
    assert grove.count_empty_ground() == 110


def test_part2():
    iter = file_to_list("tests/data/day23.txt")
    grove = GrovePlanting(iter)
    assert grove.rounds(-1) == 20
