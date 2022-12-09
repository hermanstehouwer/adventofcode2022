import pytest

from lib.read.lists import file_to_list
from lib.types.rope_bridge import RopeBridge


def test_number_visited():
    iter = file_to_list("tests/data/day9.txt")
    rope_bridge = RopeBridge()
    rope_bridge.do_moves(iter)
    assert rope_bridge.number_of_fields_visited_by_tail() == 13


@pytest.mark.parametrize("file,expected_tail_visits",[
    ("tests/data/day9.txt", 1),
    ("tests/data/day9_2.txt", 36)
])
def test_number_visited_part2(file, expected_tail_visits):
    iter = file_to_list(file)
    rope_bridge = RopeBridge(length_rope=10)
    rope_bridge.do_moves(iter)
    assert rope_bridge.number_of_fields_visited_by_tail() == expected_tail_visits

