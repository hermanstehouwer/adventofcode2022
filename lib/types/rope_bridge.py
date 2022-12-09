from typing import Tuple, Set, Iterable, AnyStr, List
from lib.types.trees import Directions


class RopeBridge:
    rope: List[Tuple[int, int]]
    visited: Set[Tuple[int, int]]

    def __init__(self, length_rope=2):
        self.rope = [(0, 0) for _ in range(length_rope)]
        self.visited = {(0, 0)}

    def do_moves(self, it: Iterable[AnyStr]) -> None:
        for line in it:
            match line.split():
                case "U", distance: self.do_move(Directions.UP, int(distance))
                case "D", distance: self.do_move(Directions.DOWN, int(distance))
                case "L", distance: self.do_move(Directions.LEFT, int(distance))
                case "R", distance: self.do_move(Directions.RIGHT, int(distance))

    def do_move(self, direction: Directions, distance: int) -> None:
        for _ in range(distance):
            old_rope = self.rope[1:]
            self.rope = [self.new_pos(self.rope[0], direction)]
            for knot in old_rope:
                prev = self.rope[-1]
                if self.knot_knot_adjecent(prev, knot):
                    self.rope.append(knot)
                else:
                    self.rope.append(self.find_new_pos(prev, knot))
            self.visited.add(self.rope[-1])

    @staticmethod
    def new_pos(pos: Tuple[int, int], direction: Directions):
        match direction:
            case Directions.UP:    return pos[0]-1, pos[1]
            case Directions.DOWN:  return pos[0]+1, pos[1]
            case Directions.LEFT:  return pos[0]  , pos[1]-1
            case Directions.RIGHT: return pos[0]  , pos[1]+1

    def number_of_fields_visited_by_tail(self) -> int:
        return len(self.visited)

    @staticmethod
    def knot_knot_adjecent(head: Tuple[int, int], tail: Tuple[int, int]) -> bool:
        return not( abs(head[0] - tail[0]) > 1 or
                    abs(head[1] - tail[1]) > 1)

    @staticmethod
    def find_new_pos(prev, knot):
        a = -1 if prev[0] < knot[0] else 1 if prev[0] > knot[0] else 0
        b = -1 if prev[1] < knot[1] else 1 if prev[1] > knot[1] else 0
        return knot[0] + a, knot[1] + b
