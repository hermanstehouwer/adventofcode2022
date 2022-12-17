from typing import AnyStr, Tuple, List, Dict


class Pyroclastic:
    rocks = [  # ALLL (x,y) with (0,0) being leftest lowest of the rock
        [(0,0),(1,0),(2,0),(3,0)],        # -
        [(1,0),(0,1),(1,1),(2,1),(1,2)],  # +
        [(0,0),(1,0),(2,0),(2,1),(2,2)],  # L (inverse)
        [(0,0),(0,1),(0,2),(0,3)],        # |
        [(0,0),(1,0),(0,1),(1,1)],        # []
    ]

    def __init__(self, jets: AnyStr, width=7):
        self.jets = [ord(j)-ord("=") for j in jets]
        self.width = width
        self.chamber = set([(x, 0) for x in range(width)])
        self.max_height = 0

    def location_is_empty(self, location: Tuple[int, int]) -> bool:
        return location[0] in range(self.width) and location not in self.chamber

    def is_valid_move(self, location: Tuple[int, int], offset: Tuple[int, int], rock: List[Tuple[int, int]]) -> bool:
        return all(self.location_is_empty((location[0] + offset[0] + r[0], location[1] + offset[1] + r[1])) for r in rock)

    def top_shape(self) -> Tuple:
        return tuple([1 if (i, self.max_height) in self.chamber else 0 for i in range(self.width)])

    def prune(self) -> None:
        # Note: min_of_max determined by trial and error. Much faster than calculating optimal value.
        # On my input 10 doesn't work for instance.
        min_of_max = self.max_height - 100
        self.chamber = {x for x in self.chamber if x[1] > min_of_max}

    def drop_rocks(self, n_rocks: int) -> None:
        j = 0
        # Dictionary of rock, jet, fingerprint (see top_shape) -> n, height(at n)
        cache: Dict[Tuple[int, int, Tuple[Tuple[int,int]]], Tuple[int, int]] = dict()
        hit = False
        offset = 0
        n = 0
        while n < n_rocks:
            p = (2, self.max_height+4)
            i = n % len(self.rocks)
            rock = self.rocks[i]

            if n % 100 == 0 and n > 0:
                self.prune()

            if not hit: # We only hit the cache once, afterwards we just complete until n == n_rocks
                cache_key = (i, j, self.top_shape())
                if cache_key in cache:
                    hit = True
                    cache_n, cache_h = cache[cache_key]
                    cycles = (n_rocks - n) // (n - cache_n)
                    offset = cycles * (self.max_height - cache_h)
                    n += (n - cache_n) * cycles
                else:
                    cache[cache_key] = (n, self.max_height)

            while True:
                jet = self.jets[j]
                j = (j + 1) % len(self.jets)

                if self.is_valid_move(p, (jet, 0), rock):
                    p = (p[0] + jet, p[1])
                if self.is_valid_move(p, (0, -1), rock):
                    p = (p[0], p[1] - 1)
                else:
                    break  # can't move down: done!
            self.chamber |= {(p[0] + r[0], p[1] + r[1]) for r in rock}
            self.max_height = max(x[1] for x in self.chamber)
            n += 1
        self.max_height += offset
