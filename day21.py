from lib.read.lists import file_to_list
from lib.types.monkey_tree import MonkeyTree

iter = file_to_list("data/day21.txt")
monkeys = MonkeyTree(iter)
print(monkeys.calculate_value())
print(monkeys.find_human_value_start())