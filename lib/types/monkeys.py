import math
from dataclasses import dataclass
from math import prod
from typing import List, Callable


@dataclass
class Item:
    worry: int


@dataclass
class Monkey:
    items: List[Item]
    operation: Callable[[int], int]
    test: int
    true_dest: int
    false_dest: int
    monkeys: 'Monkeys'
    inspect_count: int

    def take_turn(self, very_worried=False,modulo=0):
        items = self.items
        self.items = []
        for item in items:
            item.worry = self.operation(item.worry)
            self.inspect_count += 1
            if not very_worried:
                item.worry = item.worry//3
            else:
                item.worry %= modulo
            if item.worry % self.test == 0:
                self.monkeys.monkeys[self.true_dest].items.append(item)
            else:
                self.monkeys.monkeys[self.false_dest].items.append(item)


class Monkeys():
    monkeys: List[Monkey]

    def __init__(self):
        self.monkeys = []

    def add_monkey(self,
                   items: [List[int]],
                   operation: Callable[[int], int],
                   test: int,
                   true_dest: int,
                   false_dest: int,
                   ) -> None:
        self.monkeys.append(Monkey([Item(x) for x in items], operation, test, true_dest, false_dest, self, 0))

    def execute_rounds(self, rounds: int, very_worried=False) -> None:
        lcm = 0
        if very_worried:
            lcm = math.lcm(*[monkey.test for monkey in self.monkeys])
        for _ in range(rounds):
            for monkey in self.monkeys:
                monkey.take_turn(very_worried=very_worried, modulo=lcm)

    def monkey_business(self) -> int:
        return prod(sorted([m.inspect_count for m in self.monkeys])[-2:])
