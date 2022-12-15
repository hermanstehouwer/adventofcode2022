from dataclasses import dataclass
from typing import Iterator, AnyStr, Tuple, List
import re

# Sensor at x=9, y=16: closest beacon is at x=10, y=16
def manhattan(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

@dataclass
class Sensor:
    sensor: Tuple[int, int]
    beacon: Tuple[int, int]


class Beacon:
    def __init__(self, iter: Iterator[AnyStr]):
        self.sensors = []
        for line in iter:
            self.add_sensor(line)

    def add_sensor(self, line: AnyStr) -> None:
        m = re.match(r".*x=(.*), y=(.*): .*x=(.*), y=(.*)", line)
        s = (int(m.group(1)), int(m.group(2)))
        b = (int(m.group(3)), int(m.group(4)))
        self.sensors.append(Sensor(s, b))

    def excluded_on_line(self, line: int) -> int:
        ranges = self.ranges_on_line(line)
        return sum([t - f for f, t in ranges])

    def ranges_on_line(self, line: int) -> List[List[int]]:
        intervals = []
        for sensor in self.sensors:
            delta = manhattan(sensor.sensor, sensor.beacon) - abs(sensor.sensor[1] - line)
            if delta >= 0:
                intervals.append( (sensor.sensor[0] - delta, sensor.sensor[0] + delta) )

        ranges = []
        for f, t in sorted(intervals):
            if ranges and ranges[-1][1] >= f - 1:
                ranges[-1][1] = max(ranges[-1][1], t)
            else:
                ranges.append([f, t])

        return ranges

    def locate_beacon_tuning_frequency(self, max_xy: int) -> int:
        tuning = 4000000
        for line in range(max_xy+1):
            ranges = self.ranges_on_line(line)
            for r in ranges:
                if r[0] > 0:
                    if r[0]-1 <= max_xy:
                        x = r[0]-1
                        y = line
                        return x * tuning + y
                if r[1] < max_xy:
                    if r[1]+1 >= 0:
                        x = r[1]+1
                        y = line
                        return x * tuning + y
        return 0
