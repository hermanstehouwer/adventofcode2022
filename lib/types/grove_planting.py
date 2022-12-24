from collections import deque, defaultdict
from typing import Iterator, AnyStr, Dict, Tuple, Set, Deque, List

STEPS = {
    "N": (0, -1),
    "NE": (1, -1),
    "E": (1, 0),
    "SE": (1, 1),
    "S": (0, 1),
    "SW": (-1, 1),
    "W": (-1, 0),
    "NW": (-1, -1)
}

INIT_DIRECTIONS = [
    (["N", "NE", "NW"], "N"),
    (["S", "SE", "SW"], "S"),
    (["W", "NW", "SW"], "W"),
    (["E", "NE", "SE"], "E")
]


class GrovePlanting:
    def __init__(self, it: Iterator[AnyStr]):
        self.proposed_moves: Dict[Tuple[int, int], List[Tuple[int, int]]] = defaultdict(list)
        self.elves: Set[Tuple[int, int]] = set()
        self.directions: Deque[Tuple[List[AnyStr], AnyStr]] = deque(INIT_DIRECTIONS)
        for y, line in enumerate(it, start=1):
            for x, c in enumerate(line, start=1):
                if c == "#":
                    self.elves.add((x, y))

    def rounds(self, rounds: int) -> int:
        i = 0
        while i != rounds:
            i += 1
            # first half of round
            elves_round = self.elves_adjecent_elves()
            if not elves_round:
                return i
            for elf in elves_round:
                proposal = self.get_proposed_move(elf)
                if proposal is not None:
                    self.proposed_moves[proposal].append(elf)
            # second half of round
            for proposal, elves in self.proposed_moves.items():
                if len(elves) == 1:
                    self.elves.discard(elves[0])
                    self.elves.add(proposal)
            self.proposed_moves = defaultdict(list)
            self.directions.rotate(-1)
            self.count_empty_ground()

    def elves_adjecent_elves(self):
        elves = []
        for elf in self.elves:
            if any([(elf[0] + a, elf[1] + b) in self.elves for a, b in STEPS.values()]):
                elves.append(elf)
        return elves

    def count_empty_ground(self) -> int:
        x = [e[0] for e in self.elves]
        y = [e[1] for e in self.elves]
        return (max(x) - min(x) + 1) * (max(y) - min(y) + 1) - len(self.elves)

    def get_proposed_move(self, elf: Tuple[int, int]) -> Tuple[int, int] | None:
        for checks, delta in self.directions:
            if not any([(elf[0] + a, elf[1] + b) in self.elves for a, b in [STEPS[x] for x in checks]]):
                return elf[0] + STEPS[delta][0], elf[1] + STEPS[delta][1]
        return None