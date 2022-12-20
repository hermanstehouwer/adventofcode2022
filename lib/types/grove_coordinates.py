from collections import deque
from typing import Iterable, AnyStr, Dict


class GroveCoordinates:
    def __init__(self, it: Iterable[AnyStr], decryption_key: int = 1):
        self.linkedlist = deque()
        self.last_idx = 0
        for line in it:
            self.add_item(line, decryption_key)

    def add_item(self, line: AnyStr, decryption_key: int) -> None:
        val = int(line) * decryption_key
        self.linkedlist.append((self.last_idx, val))
        self.last_idx += 1

    def mix_all(self, times: int = 1) -> None:
        for _ in range(times):
            for item in range(self.last_idx):
                self.mix_item(item)

    def mix_item(self, item: int) -> None:
        while self.linkedlist[0][0] != item:
            self.linkedlist.rotate(-1)
        if self.linkedlist[0][1] == 0:
            return

        idx, val = self.linkedlist.popleft()
        self.linkedlist.rotate(-1 * val)
        self.linkedlist.appendleft((idx, val))

    def value_of_coord(self, start_item: int, steps: int):
        while self.linkedlist[0][1] != start_item:
            self.linkedlist.rotate(-1)
        for _ in range(steps):
            self.linkedlist.rotate(-1)
        return self.linkedlist[0][1]

