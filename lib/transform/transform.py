from typing import Iterator, Any


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