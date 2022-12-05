from lib.read.lists import file_to_list
from lib.types.supply_stacks import Stacks

iter = file_to_list("data/day5.txt")
stacks = Stacks()
stacks.parse(iter)
stacks.process(iter)
print(stacks.tops())

iter = file_to_list("data/day5.txt")
stacks = Stacks()
stacks.parse(iter)
stacks.process(iter, keep_order=True)
print(stacks.tops())