import pytest

from lib.read.lists import file_to_list
from lib.types.grove_coordinates import GroveCoordinates


@pytest.fixture
def grove():
    iter = file_to_list("tests/data/day20.txt")
    yield GroveCoordinates(iter)


def test_day1(grove):
    grove.mix_all()
    assert sum([grove.value_of_coord(0, x) for x in [1000, 2000, 3000]]) == 3
    assert grove.value_of_coord(0, 3) == 1
    assert grove.value_of_coord(0, 7) == 0
    assert grove.value_of_coord(0, 8) == 3
    assert grove.value_of_coord(0, 9) == -2


def test_day2(grove):
    grove = GroveCoordinates(file_to_list("tests/data/day20.txt"), decryption_key=811589153)
    grove.mix_all(times=10)
    assert sum([grove.value_of_coord(0, x) for x in [1000, 2000, 3000]]) == 1623178306
