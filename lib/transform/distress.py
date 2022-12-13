import math
from functools import cmp_to_key
from itertools import zip_longest
from typing import Iterator, AnyStr, Tuple, List


def list_to_pairs(iter: Iterator[AnyStr]) -> Iterator[Tuple[AnyStr, AnyStr]]:
    out = []
    for i in iter:
        out.append(i)
        if len(out) == 3:
            yield out[0], out[1]
            out = []
    if len(out) == 2:
        yield tuple(out)


def prep_pairs(iter: Iterator[Tuple[AnyStr, AnyStr]]) -> Iterator[Tuple[int, List[List | int], List[List | int]]]:
    count = 1
    for i in iter:
        yield count, eval(i[0]), eval(i[1])
        count += 1


def process_and_sum(iter: Iterator[Tuple[int, List[List | int], List[List | int]]]) -> int:
    return sum([i[0] for i in iter if correct_order(i[1], i[2])])


def correct_order(first: list, second: list) -> bool:
    if isinstance(first, int) and isinstance(second, int):
        if first < second: return True
        if second < first: return False
    elif isinstance(first, list) and isinstance(second, list):
        for p in zip_longest(first, second):
            if p[0] is None:
                return True
            elif p[1] is None:
                return False
            elif (out := correct_order(p[0], p[1])) is not None:
                    return out
    elif isinstance(first, int) and isinstance(second, list):
        return correct_order([first], second)
    elif isinstance(first, list) and isinstance(second, int):
        return correct_order(first, [second])


def sort_and_decode(iter: Iterator[AnyStr]) -> int:
    dividers = [[[2]], [[6]]]

    def comparator(first, second):
        c = correct_order(first, second)
        if c: return 1
        if c is None: return 0
        return -1

    packets = [eval(i) for i in iter if i != ""] + dividers
    packets.sort(key=cmp_to_key(comparator), reverse=True)
    return math.prod([i for i, p in enumerate(packets, start=1) if p in dividers])
