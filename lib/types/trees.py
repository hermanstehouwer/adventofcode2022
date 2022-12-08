from typing import Iterator, AnyStr, List, Tuple
from math import prod

directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]


def lines_to_ints(lines: Iterator[AnyStr]) -> List[List[int]]:
    ret = []
    for line in lines:
        ret.append([int(x) for x in line])
    return ret


def visible_trees(trees: List[List[int]]) -> int:
    return sum([
        visible_tree(trees, coord) for coord in
        [(x, y) for x in range(len(trees)) for y in range(len(trees[0]))]
    ])


def visible_tree(trees: List[List[int]], coord: Tuple[int, int]) -> bool:
    return any([
        is_visible(to_line_of_trees(trees, coord, d)) for d in directions
    ])


def to_line_of_trees(trees: List[List[int]], coord: Tuple[int, int], direction: Tuple[int, int]) -> List[int]:
    ret = [trees[coord[0]][coord[1]]]
    new_coord = (coord[0] + direction[0], coord[1] + direction[1])
    if not valid_coord(trees, new_coord):
        return ret
    return ret + to_line_of_trees(trees, new_coord, direction)


def is_visible(trees_line: List[int]) -> bool:
    if len(trees_line) == 1:
        return True
    first_tree = trees_line[0]
    return all(first_tree > t for t in trees_line[1:])


def valid_coord(trees: List[List[int]], coord: Tuple[int, int]) -> bool:
    if coord[0] < 0 or coord[1] < 0:
        return False
    if coord[0] >= len(trees):
        return False
    if coord[1] >= len(trees[0]):
        return False
    return True


def max_scenic_score(trees: List[List[int]]) -> int:
    return max([
        scenic_score(trees, coord) for coord in
        [(x, y) for x in range(len(trees)) for y in range(len(trees[0]))]
    ])


def scenic_score(trees: List[List[int]], coord: Tuple[int,int]) -> int:
    return prod([
        line_to_score(to_line_of_trees(trees, coord, d)) for d in directions
    ])


def line_to_score(line: List[int]) -> int:
    first_tree = line[0]
    c = 0
    for t in line[1:]:
        c+=1
        if t >= first_tree:
            return c
    return c
