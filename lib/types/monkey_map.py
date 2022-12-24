from enum import IntEnum
from itertools import groupby
from typing import Iterator, AnyStr, Dict, Tuple


class MonkeyMap:
    def __init__(self, it: Iterator[AnyStr]):
        self.map: Dict[Tuple[int, int], int] = dict()
        self.start = None
        self.direction = 0  # >: 0, v: 1, <: 2, ^:3
        self.moves = {
            0: (1, 0),
            1: (0, 1),
            2: (-1, 0),
            3: (0, -1)
        }
        for y, line in enumerate(it, start=1):
            if line == "": break
            for x, c in enumerate(line, start=1):
                if self.start is None and c == ".": self.start = (x, y)
                match c:
                    case " ": pass
                    case ".": self.map[(x, y)] = 0
                    case "#": self.map[(x, y)] = 1
                    case _: raise ValueError("EXPECTED ' ', '#', or '.'")
        self.instructions = next(it)
        self.curr = self.start

    def reset(self):
        self.curr = self.start
        self.direction = 0

    def instruction_iterator(self) -> Iterator[int | AnyStr]:
        for _, i in groupby(self.instructions, str.isalpha):
            yield "".join(list(i))

    def move_it(self, cubed: bool = False) -> None:
        for step in self.instruction_iterator():
            if step.isalpha():
                self.turn(step)
            else:
                self.move(int(step), cubed)

    def turn(self, step: AnyStr) -> None:
        if step == "R":
            self.direction = (self.direction + 1) % 4
        else:
            self.direction = (self.direction - 1) % 4

    def move(self, steps: int, cubed: bool) -> None:
        for _ in range(steps):
            self.curr = self.next_pos(cubed)

    def next_pos(self, cubed: bool) -> Tuple[int, int]:
        cand = tuple(x + y for x, y in zip(self.curr, self.moves[self.direction]))
        if cand not in self.map.keys():
            if cubed:
                cand = self.cube_wrap()
            else:
                cand = self.flat_wrap()
        if self.map[cand] == 0:
            return cand
        return self.curr

    def flat_wrap(self) -> Tuple[int, int]:
        match self.direction:
            case 0:
                return min([x[0] for x in self.map.keys() if x[1] == self.curr[1]]), self.curr[1]
            case 2:
                return max([x[0] for x in self.map.keys() if x[1] == self.curr[1]]), self.curr[1]
            case 1:
                return self.curr[0], min([x[1] for x in self.map.keys() if x[0] == self.curr[0]])
            case 3:
                return self.curr[0], max([x[1] for x in self.map.keys() if x[0] == self.curr[0]])

    def cube_wrap(self) -> Tuple[int, int]:
        return self.start

    def calc_value(self) -> int:
        return 1000 * self.curr[1] + 4 * self.curr[0] + self.direction
