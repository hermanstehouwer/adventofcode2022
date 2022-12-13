from lib.read.lists import file_to_list
from lib.transform.distress import prep_pairs, list_to_pairs, process_and_sum, sort_and_decode


def test_part1():
    iter = file_to_list("tests/data/day13.txt")
    assert process_and_sum(prep_pairs(list_to_pairs(iter))) == 13


def test_part2():
    iter = file_to_list("tests/data/day13.txt")
    assert sort_and_decode(iter) == 140