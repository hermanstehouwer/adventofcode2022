from typing import Iterator, AnyStr, Tuple


class Regiolith:
    def __init__(self, iter: Iterator[AnyStr]):
        self.map = dict()
        for line in iter:
            self.add_rock_line(line)
        self.depth = max([x[1] for x in self.map])
        self.floor = self.depth + 2

    def add_rock_line(self, line: AnyStr):
        coords = line.split(" -> ")
        for pair in zip(coords, coords[1:]):
            self.add_rock_coords(pair[0], pair[1])

    def add_rock_coords(self, f: AnyStr, t: AnyStr):
        f = tuple([int(x) for x in f.split(",")])
        t = tuple([int(x) for x in t.split(",")])
        if f[0] == t[0]:
            for y in range(min([f[1], t[1]]), max([f[1], t[1]])+1):
                self.map[(f[0], y)] = 0
        else:
            for x in range(min([f[0], t[0]]), max([f[0], t[0]])+1):
                self.map[(x, f[1])] = 0

    def simulate_pour(self, floor: bool=False) -> int:
        try: # want to break out a double loop
            while True:
                s = (500,0) # sand flows in from starting position.
                while ns := self.next_pos(s, floor):
                    s = ns
                    if s[1] == self.depth and not floor: raise Exception()
                self.map[s] = 1
                if s == (500,0): raise Exception() # Sand has blocked the entry
        except Exception:
            return sum(self.map.values())

    def next_pos(self, s: Tuple[int, int], floor: bool) -> Tuple[int, int] | None:
        for ns in [(s[0], s[1]+1), (s[0]-1, s[1]+1), (s[0]+1, s[1]+1)]:
            if ns not in self.map and ns[1] != self.floor: return ns
        return None
