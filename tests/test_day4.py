from lib.read.lists import file_to_list
from lib.transform.transform import split_two, to_range, overlap_all_sets, overlap_partial_sets


def test_overlap():
    a = map(lambda x: map(to_range,x),
        split_two(file_to_list("tests/data/day4.txt"), split=","))
    b = filter(overlap_all_sets,a)
    assert 2==len(list(b))


def test_partial_overlap():
    a = map(lambda x: map(to_range, x),
            split_two(file_to_list("tests/data/day4.txt"), split=","))
    b = filter(overlap_partial_sets, a)
    assert 4 == len(list(b))