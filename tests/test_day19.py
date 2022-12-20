from lib.read.lists import file_to_list
from lib.types.blueprint import BluePrint
import pytest


@pytest.mark.skip("takes too long")
def test_part1():
    iter = file_to_list("tests/data/day19.txt")
    assert BluePrint(next(iter)).quality_level(24) == 9
    assert BluePrint(next(iter)).quality_level(24) == 24
