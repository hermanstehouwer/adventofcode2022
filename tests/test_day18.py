from lib.read.lists import file_to_list
from lib.types.droplet import Droplet
from pytest import fixture


@fixture
def droplet():
    iter = file_to_list("tests/data/day18.txt")
    yield Droplet(iter)


def test_part1(droplet):
    assert droplet.calculate_sides() == 64


def test_part2(droplet):
    assert droplet.calculate_surface() == 58
