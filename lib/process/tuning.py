from typing import Iterator, AnyStr, List


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


def rec_lockon_tuning(iter: Iterator[AnyStr], comp: List[AnyStr], target_lenght: int = 4, idx: int = 0) -> int:
    if len(comp) != target_lenght:  # it's always too short; just append.
        return rec_lockon_tuning(iter, target_lenght=target_lenght, idx=idx+1, comp=comp + [next(iter)])
    if len(comp) == len(set(comp)):
        return idx
    return rec_lockon_tuning(iter, target_lenght=target_lenght, idx=idx+1, comp=comp[1:] + [next(iter)])
