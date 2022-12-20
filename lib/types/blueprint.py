from enum import IntEnum
from functools import lru_cache
from typing import AnyStr
import re


class RobotIDX(IntEnum):
    ORE: 0
    CLAY: 1
    OBSIDIAN: 2
    GEODE: 3


class BluePrint:
    # (ROBOTS, RESOURCES, COSTS((...)(...)(...)(...)))
    def __init__(self, description: AnyStr):
        r = r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian."
        m = re.match(r, description)
        self.blueprint_number = int(m.group(1))
        self.robots = (1,0,0,0)     # Start with one ORE robot
        self.resources = (0,0,0,0)  # Start with no resources
        self.costs = ((int(m.group(2)), 0, 0, 0),
                      (int(m.group(3)), 0, 0, 0),
                      (int(m.group(4)), int(m.group(5)), 0, 0),
                      (int(m.group(6)), 0, int(m.group(7)), 0))

    @lru_cache
    def max_consumed(self, robot):
        return max([x[robot] for x in self.costs])

    def quality_level(self, minutes: int) -> int:
        start_state = (self.robots, self.resources, minutes)
        queue = [start_state]
        cache = set()
        results = 0
        while queue:
            robots, resources, minutes_left = queue.pop()
            # do not process same(ish) state twice if you had a better run.
            cache_key = (robots, resources, minutes_left)
            if cache_key in cache:
                continue
            if results > resources[3] + robots[3] * minutes_left + (minutes_left * (minutes_left - 1)) // 2:
                # If we cannot produce enough GEODE to win when producing a geode robot every minute.
                continue
            cache.add(cache_key)
            # Do nothing state.
            new_resources = tuple(rs + rb for rs, rb in zip(resources, robots))
            new_minutes_left = minutes_left - 1
            if new_minutes_left == 0:
                if new_resources[3] > results:
                    results = new_resources[3]
                continue
            for rbt in [3, 2, 1, 0]:
                # Try to reach next state in which you have build a robot.
                # NOTE: check against previous_state_resources. Calculate on new resources!
                if min(rs - rb for rs, rb in zip(resources, self.costs[rbt])) < 0:
                    continue
                # If we already produce more resources than we can consume ...
                if rbt != 3 and robots[rbt] >= self.max_consumed(rbt):
                    continue
                queue.append((
                    (robots[0] + (1,0,0,0)[rbt], robots[1] + (0,1,0,0)[rbt], robots[2] + (0,0,1,0)[rbt], robots[3] + (0,0,0,1)[rbt] ),
                    tuple(rs - rb for rs, rb in zip(new_resources, self.costs[rbt])),
                    new_minutes_left
                ))
                continue
            queue.append((robots, new_resources, new_minutes_left))
        return results
