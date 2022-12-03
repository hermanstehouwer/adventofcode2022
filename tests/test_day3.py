import pytest

from lib.transform.transform import split_middle, tuple_to_unique_character, char_to_priority, iter_split_middle, \
    iter_tuple_to_unique_character, iter_char_to_priority, iter_group


@pytest.mark.parametrize("input,error_character", [
    ("vJrwpWtwJgWrhcsFMMfFFhFp", "p"),
    ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "L"),
    ("PmmdzqPrVvPwwTWBwg", "P"),
    ("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "v"),
    ("ttgJtRGJQctTZtZT", "t"),
    ("CrZsJsPPZsGzwwsLwLmpwMDw", "s")
])
def test_find_correct_error(input, error_character):
    assert tuple_to_unique_character(split_middle(input)) == error_character


@pytest.mark.parametrize("input,expected_priority", [
    ("vJrwpWtwJgWrhcsFMMfFFhFp", 16),
    ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", 38),
    ("PmmdzqPrVvPwwTWBwg", 42),
    ("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", 22),
    ("ttgJtRGJQctTZtZT", 20),
    ("CrZsJsPPZsGzwwsLwLmpwMDw", 19)
])
def test_find_correct_priority(input, expected_priority):
    assert char_to_priority(tuple_to_unique_character(split_middle(input))) == expected_priority


def test_sum_of_priorities():
    input = ["vJrwpWtwJgWrhcsFMMfFFhFp",
             "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
             "PmmdzqPrVvPwwTWBwg",
             "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
             "ttgJtRGJQctTZtZT",
             "CrZsJsPPZsGzwwsLwLmpwMDw"]
    assert sum(iter_char_to_priority(iter_tuple_to_unique_character(iter_split_middle(input)))) == 157

def test_sum_of_badge_priorities():
    input = ["vJrwpWtwJgWrhcsFMMfFFhFp",
             "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
             "PmmdzqPrVvPwwTWBwg",
             "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
             "ttgJtRGJQctTZtZT",
             "CrZsJsPPZsGzwwsLwLmpwMDw"]
    assert sum(iter_char_to_priority(iter_tuple_to_unique_character(iter_group(iter(input))))) == 70

