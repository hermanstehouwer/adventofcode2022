from lib.read.lists import file_to_list
from lib.types.monkey_map import MonkeyMap

iter = file_to_list("data/day22.txt")
monkey_map = MonkeyMap(iter)
monkey_map.move_it()
print(monkey_map.calc_value())
