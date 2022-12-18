from typing import Iterable, AnyStr, Tuple, List


class Droplet:
    def __init__(self, iter: Iterable[AnyStr]):
        self.drops = set()
        for line in iter:
            a, b, c = line.split(",")
            self.drops |= {tuple([int(a), int(b), int(c)])}
        max_a = max([c[0] for c in self.drops]) + 2 # One for steam on the outside
        max_b = max([c[1] for c in self.drops]) + 2 # And one for the range()
        max_c = max([c[2] for c in self.drops]) + 2
        self.max_max = max([max_a, max_b, max_c])

    def get_nbrs(self, coord: Tuple[int, int, int]) -> List[Tuple[int, int, int]]:
        a, b, c = coord
        nbrs = []
        for delta in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
            nbr = (a + delta[0], b + delta[1], c + delta[2])
            # Let op! ook de -1: hij moet er langs en er onderdoor kunnen!
            if all(-1 <= c <= self.max_max for c in nbr):
                nbrs.append(nbr)
        return nbrs

    def calculate_sides(self) -> int:
        count = 0
        for drop in self.drops:
            for check in self.get_nbrs(drop):
                if check not in self.drops:
                    count+=1
        return count

    def calculate_surface(self) -> int:
        steam_area = {(0, 0, 0)}
        queue = [(0,0,0)]
        count = 0
        while queue:
            curr = queue.pop()
            for nbr in self.get_nbrs(curr):
                if nbr in self.drops:
                    count += 1
                else:
                    if nbr not in steam_area:
                        steam_area |= {nbr}
                        queue.append(nbr)
        return count
