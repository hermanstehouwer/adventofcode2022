import copy

from lib.types.monkeys import Monkeys

monkeys = Monkeys()
monkeys.add_monkey([91, 54, 70, 61, 64, 64, 60, 85], lambda x: x * 13, 2, 5, 2)
monkeys.add_monkey([82], lambda x: x + 7, 13, 4, 3)
monkeys.add_monkey([84, 93, 70], lambda x: x + 2, 5, 5, 1)
monkeys.add_monkey([78, 56, 85, 93], lambda x: x * 2, 3, 6, 7)
monkeys.add_monkey([64, 57, 81, 95, 52, 71, 58], lambda x: x * x, 11, 7, 3)
monkeys.add_monkey([58, 71, 96, 58, 68, 90], lambda x: x + 6, 17, 4, 1)
monkeys.add_monkey([56, 99, 89, 97, 81], lambda x: x + 1, 7, 0, 2)
monkeys.add_monkey([68, 72], lambda x: x + 8, 19, 6, 0)

monkeys2 = copy.deepcopy(monkeys)

monkeys.execute_rounds(20)
print(monkeys.monkey_business())

monkeys2.execute_rounds(10000, very_worried=True)
print(monkeys2.monkey_business())
