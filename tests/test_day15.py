from lib.read.lists import file_to_list
from lib.types.beacon import Beacon
import pytest

@pytest.fixture
def beacon():
    iter = file_to_list("tests/data/day15.txt")
    yield Beacon(iter)


def test_part1(beacon):
    assert beacon.excluded_on_line(10) == 26


def test_part2(beacon):
    assert beacon.locate_beacon_tuning_frequency(20) == 56000011