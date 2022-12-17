import itertools
from heapq import heappush, heappop
from typing import AnyStr, Iterator, List, Set, Dict, Tuple
import re


class Valve:
    def __init__(self, descriptor: AnyStr):
        m = re.match(r"Valve (.*) has flow rate=(.*); tunnels? leads? to valves? (.*)", descriptor)
        self.name = m.group(1)
        self.flow_rate = int( m.group(2) )
        self.tunnels = [c for c in m.group(3).split(", ")]


class Pipes:
    def __init__(self, iter: Iterator[AnyStr]):
        self.pipes = dict()
        for line in iter:
            valve = Valve(line)
            self.pipes[valve.name] = valve
        self.paths = dict()
        self.calculate_all_paths()

    def calculate_all_paths(self):
        for valve in self.pipes:
            self.calculate_all_paths2(valve)

    def calculate_all_paths2(self, source):
        distances = {source: 0}
        previous = {}
        queue = []
        for valve in self.pipes:
            if valve != source:
                distances[valve] = 9999
            heappush(queue, (distances[valve], valve))

        while queue:
            _, current = heappop(queue)
            for nbr in self.pipes[current].tunnels:
                new_dist = distances[current] + 1
                if new_dist < distances[nbr]:
                    distances[nbr] = new_dist
                    previous[nbr] = current
                    heappush(queue, (distances[nbr], nbr))

        distances.pop(source)
        self.paths[source] = distances

    def max_pressure_released(self, minutes=30, elephant=False) -> int:
        def generate_paths(path_so_far: List[AnyStr], unopened: Set[AnyStr], time_left) -> Iterator[List[AnyStr]]:
            yield path_so_far
            prev = path_so_far[-1]
            for next in unopened:
                if self.paths[prev][next] < time_left - 1:
                    yield from generate_paths(
                        path_so_far+[next],
                        unopened - {next},
                        time_left = time_left - (self.paths[prev][next] + 1)
                    )
        all_paths = generate_paths(["AA"], set([x for x in self.pipes.keys() if self.pipes[x].flow_rate > 0]), minutes)

        def value_of_path(curr: AnyStr, path: List[AnyStr], time_left: int, pressure: int = 0):
            if path:
                nxt = path[0]
                rst = path[1:]
                time_left -= (self.paths[curr][nxt] + 1)
                pressure += time_left * self.pipes[nxt].flow_rate
                return value_of_path(nxt, rst, time_left, pressure)
            else:
                return pressure
        values: Dict[Tuple[AnyStr], int] = dict()
        for path in all_paths:
            v = value_of_path(path[0], path[1:], minutes)
            # NOTE: first step on path is always AA, we don't need this.
            s_path = tuple(sorted(path[1:]))
            cur_v = values.get(s_path, 0)
            if v > cur_v:
                values[s_path] = v
        if not elephant:
            return max(values.values())

        max_found = 0
        for c1, c2 in itertools.product(values.keys(), values.keys()):
            if not set(c1).intersection(set(c2)):
                val = values[c1] + values[c2]
                max_found = val if val > max_found else max_found
        return max_found
