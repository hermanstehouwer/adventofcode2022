from enum import IntEnum
from typing import Iterator, AnyStr, List, Tuple
from math import prod


class Directions(IntEnum):
    RIGHT = 0
    LEFT  = 1
    UP    = 2
    DOWN  = 3

    def invert(self) -> 'Directions':
        match self:
            case Directions.UP: return Directions.DOWN
            case Directions.DOWN: return Directions.UP
            case Directions.LEFT: return Directions.RIGHT
            case Directions.RIGHT: return Directions.LEFT


def lines_to_ints(lines: Iterator[AnyStr]) -> List[List[int]]:
    return [[int(x) for x in line] for line in lines]


def visible_trees(trees: List[List[int]]) -> int:
    return sum([
        visible_tree(trees, coord) for coord in
        [(x, y) for x in range(len(trees)) for y in range(len(trees[0]))]
    ])


def visible_tree(trees: List[List[int]], coord: Tuple[int, int]) -> bool:
    return any([
        is_visible(to_line_of_trees(trees, coord, d)) for d in Directions
    ])


def to_line_of_trees(trees: List[List[int]], coord: Tuple[int, int], direction: Directions) -> List[int]:
    match direction:
        case Directions.RIGHT:
            return trees[coord[0]][coord[1]:]
        case Directions.LEFT:
            return list(reversed(trees[coord[0]][:coord[1]+1]))
        case Directions.DOWN:
            return [t[coord[1]] for t in trees][coord[0]:]
        case Directions.UP:
            return list(reversed([t[coord[1]] for t in trees][:coord[0]+1]))


def is_visible(trees_line: List[int]) -> bool:
    return all(trees_line[0] > t for t in trees_line[1:])


def valid_coord(trees: List[List[int]], coord: Tuple[int, int]) -> bool:
    return not(coord[0] < 0 or coord[1] < 0 or coord[0] >= len(trees) or coord[1] >= len(trees[0]))


def max_scenic_score(trees: List[List[int]]) -> int:
    return max([
        scenic_score(trees, coord) for coord in
        [(x, y) for x in range(len(trees)) for y in range(len(trees[0]))]
    ])


def scenic_score(trees: List[List[int]], coord: Tuple[int,int]) -> int:
    return prod([
        line_to_score(to_line_of_trees(trees, coord, d)) for d in Directions
    ])


def line_to_score(line: List[int], ft = None, c = 0) -> int:
    if ft is None:
        return line_to_score(line[1:], line[0], 0)
    if not line:
        return c
    if line[0] >= ft:
        return c+1
    return line_to_score(line[1:], ft, c+1)

