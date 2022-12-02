from enum import Enum
from typing import AnyStr, List, Iterator


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def iter_to_RPS(iter: Iterator[List[AnyStr]]) -> Iterator[List[RPS]]:
    for i in iter:
        yield [to_RPS(i[0]), to_RPS(i[1])]


def to_RPS(rps: AnyStr):
    match rps:
        case "A" | "X":
            return RPS.ROCK
        case "B" | "Y":
            return RPS.PAPER
        case "C" | "Z":
            return RPS.SCISSORS


def iter_to_new_strat(iter: Iterator[List[RPS]]) -> Iterator[List[RPS]]:
    for i in iter:
        yield to_new_strat(i[0], i[1])


def to_new_strat(a: RPS, b:RPS) -> List[RPS]:
    match b:
        case RPS.ROCK: #lose
            return [a, RPS( (a.value+1) % 3 +1 )]
        case RPS.PAPER: #draw
            return [a, a]
        case RPS.SCISSORS: #win
            return [a, RPS( (a.value) % 3 + 1 )]


win_table = [
    3,0,6,
    6,3,0,
    0,6,3]


def score_round(a: RPS, b: RPS) -> int:
    return b.value + win_table[ (b.value-1)*3 + a.value -1]
