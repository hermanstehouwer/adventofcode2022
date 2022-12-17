from lib.read.lists import file_to_list
from lib.types.valves import Pipes
from pytest import fixture

@fixture
def pipes():
    iter = file_to_list("tests/data/day16.txt")
    yield Pipes(iter)


def test_part1(pipes):
    assert pipes.max_pressure_released(30) == 1651


def test_part2(pipes):
    assert pipes.max_pressure_released(26, elephant=True) == 1707
