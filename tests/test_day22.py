from lib.read.lists import file_to_list
from lib.types.monkey_map import MonkeyMap
import pytest


@pytest.fixture
def monkey_map():
    iter = file_to_list("tests/data/day22.txt")
    return MonkeyMap(iter)


def test_part1(monkey_map):
    monkey_map.move_it()
    assert monkey_map.calc_value() == 6032


@pytest.mark.skip("Not implemented yet")
def test_part2(monkey_map):
    monkey_map.move_it(cubed=True)
    assert monkey_map.calc_value() == 5031
