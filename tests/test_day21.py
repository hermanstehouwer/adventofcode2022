from lib.read.lists import file_to_list
from lib.types.monkey_tree import MonkeyTree
import pytest

@pytest.fixture
def monkeys():
    iter = file_to_list("tests/data/day21.txt")
    return MonkeyTree(iter)


def test_part1(monkeys):
    assert monkeys.calculate_value() == 152


def test_part2(monkeys):
    assert monkeys.find_human_value_start() == 301
