import pytest

from lib.read.lists import file_to_list
from lib.types.supply_stacks import Stacks


def test_stacking_stacks():
    iter = file_to_list("tests/data/day5.txt")
    stacks = Stacks()
    stacks.parse(iter)
    assert stacks.tops() == "NDP"

    stacks.process(iter)
    assert stacks.tops() == "CMZ"

def test_stacking_cratemover_9001():
    iter = file_to_list("tests/data/day5.txt")
    stacks = Stacks()
    stacks.parse(iter)
    stacks.process(iter, keep_order=True)
    assert stacks.tops() == "MCD"