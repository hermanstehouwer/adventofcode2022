from collections import defaultdict
from dataclasses import dataclass, field
from math import lcm
from queue import PriorityQueue
from typing import Iterator, AnyStr, Dict, Set, Tuple, List


class Blizzard:
    def __init__(self, it: Iterator[AnyStr]):
        self.field = set()
        self.death_start = defaultdict(list)
        self.start = None
        self.end = None

        self.width = 0
        self.height = 0

        self.init_field(it)

        self.lcm = lcm(self.width - 2, self.height - 2)
        # precompute all blizzard positions for the loop
        self.init_death()

    def init_field(self, it):
        for y, line in enumerate(it):
            self.width = len(line)
            for x, c in enumerate(line):
                match c:
                    case ".":
                        self.field.add((x, y))
                        if self.start is None:
                            self.start = (x, y)
                        self.end = (x, y)
                    case z if z in "><v^":
                        self.field.add((x, y))
                        self.death_start[z].append((x, y))
                    case "#":
                        pass
                    case _:
                        raise ValueError(f"INVALID INPUT: {c}")
                self.height = y + 1

    def init_death(self):
        self.death: Dict[int, Set[Tuple[int, int]]] = defaultdict(set)
        for direction, start_locations in self.death_start.items():
            for start_location in start_locations:
                for i in range(self.lcm):
                    self.death[i].add(start_location)
                    match direction:
                        case ">":
                            new_x = start_location[0] + 1
                            if new_x == self.width - 1:
                                new_x = 1
                            start_location = (new_x, start_location[1])
                        case "<":
                            new_x = start_location[0] - 1
                            if new_x == 0:
                                new_x = self.width - 2
                            start_location = (new_x, start_location[1])
                        case "v":
                            new_y = start_location[1] + 1
                            if new_y == self.height - 1:
                                new_y = 1
                            start_location = (start_location[0], new_y)
                        case "^":
                            new_y = start_location[1] - 1
                            if new_y == 0:
                                new_y = self.height - 2
                            start_location = (start_location[0], new_y)
                        case _:
                            raise ValueError(f"unknown direction: {direction}")

    def lenght_fastest_path(self, forgot_snacks=False) -> int:
        time = self.length_fasted_path_from_to(self.start, self.end, 0)
        if forgot_snacks:
            time = self.length_fasted_path_from_to(self.end, self.start, time)
            time = self.length_fasted_path_from_to(self.start, self.end, time)
        return time

    def length_fasted_path_from_to(self, start: Tuple[int, int], end: Tuple[int, int], start_time: int) -> int:
        queue = PriorityQueue()
        queue.put((start_time, start))
        history = set()
        while not queue.empty():
            curr_time, curr_position = queue.get()
            if curr_position == end:
                return curr_time
            candidates = self.get_nbrs_at_time(curr_position, curr_time + 1)
            for c in candidates:
                toput = curr_time + 1, c
                if toput not in history:
                    history.add(toput)
                    queue.put(toput)


    def get_nbrs_at_time(self, curr_position: Tuple[int, int], time: int) -> List[Tuple[int, int]]:
        nbrs = []
        directions = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
        for d in directions:
            candidate = curr_position[0] + d[0], curr_position[1] + d[1]
            if candidate in self.field and candidate not in self.death[time % self.lcm]:
                nbrs.append(candidate)
        return nbrs
