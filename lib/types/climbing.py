from collections import defaultdict
from dataclasses import dataclass
from queue import PriorityQueue
from typing import List, AnyStr, Iterator, Callable, Dict


@dataclass
class Coord:
    x: int
    y: int

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other: 'Coord') -> bool:
        return self.x == other.x and self.y == other.y

    def __lt__(self, other: 'Coord') -> bool:
        return self.x < other.x or self.x == other.x and self.y < other.y

class Climbing():
    map: List[List[AnyStr]]
    max_x: int
    max_y: int

    def __init__(self, iter: Iterator[AnyStr]):
        self.map = []
        for line in iter:
            self.map.append(list(line))
        self.max_x = len(self.map[0])
        self.max_y = len(self.map)

    def find_start(self):
        return self.find_coord("S")

    def find_end(self):
        return self.find_coord("E")

    def find_coord(self, target: AnyStr) -> Coord:
        for y in range(self.max_y):
            for x in range(self.max_x):
                if self.map[y][x] == target:
                    return Coord(x, y)

    def find_all(self, target: AnyStr):
        found = []
        for y in range(self.max_y):
            for x in range(self.max_x):
                if self.map[y][x] == target:
                    found.append(Coord(x, y))
        return found

    @staticmethod
    def mannhattan(f: Coord, t: Coord) -> int:
        return abs(f.x - t.x) + abs(f.y - t.y)

    def lenght_shortest_path_to_signal(self) -> int:
        return self.start_a_star([self.find_start()])

    def lenght_scenic_path_to_signal(self) -> int:
        starts = [self.find_start()] + self.find_all("a")
        return self.start_a_star(starts)

    def start_a_star(self, starts: List[Coord]):
        scores = []
        for start in starts:
            end = self.find_end()
            goal = lambda x: x == end
            h = lambda x: self.mannhattan(end, x)
            # Note: we are looking for the number of steps. So len - 1
            path = self.A_Star(start, goal, h)
            if path:
                scores.append(len(path) - 1)
        return min(scores)

    def A_Star(self, start: Coord, goal: Callable[[Coord], bool], h: Callable[[Coord], int]) -> List[AnyStr]:
        open_set = PriorityQueue()
        open_set.put((h(start), start))
        in_open_set = {start}
        came_from = dict()
        g_score = defaultdict(lambda: 99999)
        g_score[start] = 0
        f_score = defaultdict(lambda: 99999)
        f_score[start] = h(start)
        while not open_set.empty():
            current_score, current = open_set.get()
            in_open_set.discard(current)
            if goal(current):
                return self.reconstruct_path(came_from, current)
            for nbr in self.get_nbrs(current):
                tentative_g = g_score[current] + 1
                if tentative_g < g_score[nbr]:
                    came_from[nbr] = current
                    g_score[nbr] = tentative_g
                    f_score[nbr] = tentative_g + h(nbr)
                    if nbr not in in_open_set:
                        open_set.put((f_score[nbr], nbr))
                        in_open_set.add(nbr)

    def reconstruct_path(self, came_from: Dict[Coord, Coord], current: Coord) -> List[AnyStr]:
        path = [self.map[current.y][current.x]]
        while current in came_from:
            current = came_from[current]
            path.insert(0, self.map[current.y][current.x])
        return path

    def get_nbrs(self, current: Coord) -> List[Coord]:
        candidates = [Coord(current.x+1, current.y),
                      Coord(current.x-1, current.y),
                      Coord(current.x, current.y+1),
                      Coord(current.x, current.y-1)]
        candidates = [c for c in candidates if 0 <= c.x < self.max_x and 0 <= c.y < self.max_y]
        candidates = [c for c in candidates if self.get_height(c) <= self.get_height(current) + 1]
        return candidates

    def get_height(self, coord: Coord) -> int:
        match self.map[coord.y][coord.x]:
            case "S": return 0
            case "E": return 25
            case c: return ord(c) - ord("a")
