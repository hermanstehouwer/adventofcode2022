from typing import AnyStr
import pytest

from lib.read.lists import file_to_list
from lib.transform.snafu import snafu2int, int2snafu


@pytest.mark.parametrize("snafu, expected",[
                        ["1=-0-2", 1747],
                        ["12111", 906],
                        ["2=0=", 198],
                        ["21", 11],
                        ["2=01", 201],
                        ["111", 31],
                        ["20012", 1257],
                        ["112", 32],
                        ["1=-1=", 353],
                        ["1-12", 107],
                        ["12", 7],
                        ["1=", 3],
                        ["122", 37]])
def test_snafu_2_int(snafu: AnyStr, expected: int):
    assert snafu2int(snafu) == expected

@pytest.mark.parametrize("number, snafu",[
                        [1,"1"],
                        [2,"2"],
                        [3,"1="],
                        [4,"1-"],
                        [5,"10"],
                        [6,"11"],
                        [7,"12"],
                        [8,"2="],
                        [9,"2-"],
                        [10,"20"],
                        [15,"1=0"],
                        [20,"1-0"],
                        [2022,"1=11-2"],
                        [12345,"1-0---0"],
                        [314159265,"1121-1110-1=0"]])
def test_int_2_snafu(number: int, snafu: AnyStr):
    assert int2snafu(number) == snafu


def test_part1():
    iter = file_to_list("tests/data/day25.txt")
    snafu = sum(map(snafu2int, iter))
    assert snafu == 4890
    assert int2snafu(snafu) == "2=-1=0"
