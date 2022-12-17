import pytest
from lib.types.pyroclastic import Pyroclastic

@pytest.fixture
def pyro():
    yield Pyroclastic(">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>")


def test_part1(pyro: Pyroclastic):
    pyro.drop_rocks(2022)
    assert pyro.max_height == 3068


def test_part2(pyro: Pyroclastic):
    pyro.drop_rocks(1000000000000)
    assert pyro.max_height == 1514285714288
