from typing import Iterator, AnyStr, List, Tuple, Set
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


def split_two(iter: Iterator[AnyStr], split: AnyStr = " ") -> Iterator[List[AnyStr]]:
    for i in iter:
        yield i.split(split)


def iter_group(iter: Iterator[AnyStr], size_of_group: int = 3) -> Iterator[Tuple[AnyStr, AnyStr, AnyStr]]:
    y = []
    for i in iter:
        y.append(i)
        if len(y) == size_of_group:
            yield tuple(y)
            y = []


def split_middle(i: AnyStr) -> Tuple[AnyStr, AnyStr]:
    return i[:len(i) // 2], i[len(i) // 2:]


def tuple_to_unique_character(tuple: Iterator[AnyStr]) -> AnyStr:
    overlap = set(string.ascii_letters)
    for s in tuple:
        overlap = set(s) & overlap
    return overlap.pop()


def char_to_priority(input: AnyStr) -> int:
    val = ord(input) - 38
    if val > 52:
        val = val - 58
    return val


def to_range(input: AnyStr) -> Set[int]:
    a, b = input.split("-")
    return set(range(int(a), int(b)+1))


def overlap_all_sets(iter: Iterator[Set[int]]) -> bool:
    sets = list(iter)
    if sets[0].issubset(sets[1]) or sets[1].issubset(sets[0]):
        return True
    return False


def overlap_partial_sets(iter: Iterator[Set[int]]) -> bool:
    sets = list(iter)
    newset = sets[0].union(sets[1])
    return len(newset) < len(sets[0]) + len(sets[1])
