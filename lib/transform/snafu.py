from typing import AnyStr

from lib.read.lists import file_to_list


def snafu2int(snafu: AnyStr) -> int:
    base = 1
    total = 0
    for c in reversed(snafu):
        match c:
            case "0": pass
            case "1": total += base
            case "2": total += base * 2
            case "-": total -= base
            case "=": total -= base * 2
        base *= 5
    return total


def int2snafu(curr: int) -> AnyStr:
    to_string = []
    while curr:
        rem = (curr % 5)
        curr = curr // 5
        match rem:
            case 0: to_string.append("0")
            case 1: to_string.append("1")
            case 2: to_string.append("2")
            case 3:
                to_string.append("=")
                curr += 1
            case 4:
                to_string.append("-")
                curr += 1
    return "".join(reversed(to_string))
