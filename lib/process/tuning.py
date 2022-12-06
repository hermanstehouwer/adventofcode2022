from typing import Iterator, AnyStr


def lockon_tuning(iter: Iterator[AnyStr], target_lenght: int = 4) -> int:
    idx = 0
    comp = []
    while len(comp) < target_lenght:
        comp.append(next(iter))
        idx += 1
    while len(comp) != len(set(comp)):
        comp.append(next(iter))
        comp.pop(0)
        idx += 1
    return idx