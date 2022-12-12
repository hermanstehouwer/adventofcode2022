import pytest
from lib.read.lists import file_to_list
from lib.types.climbing import Climbing

@pytest.fixture
def climber():
    iter = file_to_list("tests/data/day12.txt")
    yield Climbing(iter)


def test_init_map(climber):
    assert climber.max_y == 5
    assert climber.max_x == 8


def test_part1(climber):
    assert climber.lenght_shortest_path_to_signal() == 31


def test_part2(climber):
    assert climber.lenght_scenic_path_to_signal() == 29
