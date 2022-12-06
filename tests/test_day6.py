import pytest

from lib.process.tuning import lockon_tuning, rec_lockon_tuning


@pytest.mark.parametrize("input,expected_index",[
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
    ("nppdvjthqldpwncqszvftbrmjlhg", 6),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7)
])
def test_lockon(input, expected_index):
    assert lockon_tuning(iter(input)) == expected_index
    assert rec_lockon_tuning(iter(input), []) == expected_index

@pytest.mark.parametrize("input,expected_index",[
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
    ("nppdvjthqldpwncqszvftbrmjlhg", 23),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26)
])
def test_lockon_part2(input, expected_index):
    assert lockon_tuning(iter(input), target_lenght=14) == expected_index
    assert rec_lockon_tuning(iter(input), [], target_lenght=14) == expected_index
