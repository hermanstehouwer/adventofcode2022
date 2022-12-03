from typing import Iterator, AnyStr, List, Tuple
import string


def to_int(iter: Iterator[str]) -> Iterator[int]:
    for i in iter:
        if i == "":
            yield None
        else:
            yield int(i)


def add_lists_seperated_empty_line(iter: Iterator[int]) -> Iterator[int]:
    total = 0
    for i in iter:
        if i:
            total += i
        else:
            yield total
            total = 0
    yield total


def split_two(iter: Iterator[AnyStr]) -> Iterator[List[AnyStr]]:
    for i in iter:
        yield i.split(" ")


def iter_group(iter: Iterator[AnyStr], size_of_group: int = 3) -> Iterator[Tuple[AnyStr, AnyStr, AnyStr]]:
    y = []
    for i in iter:
        y.append(i)
        if len(y) == size_of_group:
            yield tuple(y)
            y = []


def iter_split_middle(iter: Iterator[AnyStr]) -> Iterator[Tuple[AnyStr, AnyStr]]:
    for i in iter:
        yield split_middle(i)


def split_middle(i: AnyStr) -> Tuple[AnyStr, AnyStr]:
    return i[:len(i) // 2], i[len(i) // 2:]


def iter_tuple_to_unique_character(iter: Iterator[Iterator[AnyStr]]) -> Iterator[AnyStr]:
    for i in iter:
        yield tuple_to_unique_character(i)


def tuple_to_unique_character(tuple: Iterator[AnyStr]) -> AnyStr:
    overlap = set(string.ascii_letters)
    for s in tuple:
        overlap = set(s) & overlap
    return overlap.pop()


def iter_char_to_priority(iter: Iterator[AnyStr]) -> Iterator[int]:
    for i in iter:
        yield char_to_priority(i)


def char_to_priority(input: AnyStr) -> int:
    val = ord(input) - 38
    if val > 52:
        val = val - 58
    return val

