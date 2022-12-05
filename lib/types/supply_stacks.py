from typing import Iterator, AnyStr, Tuple
import re

class Stacks():
    stacks = None

    def __init__(self):
        self.stacks = []

    # parses the start After this the iterator will contain instructions!
    def parse(self, iter: Iterator[AnyStr]) -> None:
        while (l := next(iter)) != "":
            self.parse_line(l)
        for stack in self.stacks:
            stack.pop()
            stack.reverse()

    def parse_line(self, line: AnyStr) -> None:
        char_idx = 1
        stack_idx = 0
        while char_idx < len(line):
            c = line[char_idx]
            if c != " ":
                while stack_idx >= len(self.stacks):
                    self.stacks.append([])
                self.stacks[stack_idx].append(c)
            char_idx += 4
            stack_idx += 1

    def process(self, iter: Iterator[AnyStr], keep_order: bool = False) -> None:
        for i in iter:
            self.process_line(i, keep_order)

    def process_line(self, line: AnyStr, keep_order: bool = False) -> None:
        n, f, t = self.get_nft(line)
        if not keep_order:
            for _ in range(n):
                self.stacks[t].append(self.stacks[f].pop())
        else:
            to_move = self.stacks[f][-n:]
            self.stacks[f] = self.stacks[f][:-n]
            self.stacks[t].extend(to_move)

    def get_nft(self, line: AnyStr) -> Tuple[int]:
        regex = r"move (\d+) from (\d+) to (\d+)"
        m = re.match(regex, line)
        n, f, t = m.groups()
        n = int(n)
        f = int(f)
        t = int(t)
        f -= 1
        t -= 1
        return n, f, t


    def tops(self) -> AnyStr:
        a = [x[-1] for x in self.stacks]
        return "".join(a)
