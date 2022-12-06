import pytest

from lib.process.tuning import lockon_tuning


@pytest.mark.parametrize("input,expected_index",[
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
    ("nppdvjthqldpwncqszvftbrmjlhg", 6),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7)
])
def test_lockon(input, expected_index):
    assert lockon_tuning(iter(input)) == expected_index