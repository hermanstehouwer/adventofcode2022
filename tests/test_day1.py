from lib.read.lists import file_to_list
from lib.transform.transform import add_lists_seperated_empty_line, to_int


def test_day1():
    # elf with most calories has 24000
    assert max(
            add_lists_seperated_empty_line(
                to_int(file_to_list("tests/data/day1.txt"))
            )
    ) == 24000

    # top 3 elves have 45000 together
    a = list(
            add_lists_seperated_empty_line(
                to_int(file_to_list("tests/data/day1.txt"))
            )
    )
    a.sort()
    out = sum(a[-3:])
    assert out == 45000