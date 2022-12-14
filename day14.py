from lib.read.lists import file_to_list
from lib.types.regiolith import Regiolith

lines = file_to_list("data/day14.txt")
rl = Regiolith(iter(lines))
print(rl.simulate_pour())

lines = file_to_list("data/day14.txt")
rl = Regiolith(iter(lines))
print(rl.simulate_pour(floor=True))
