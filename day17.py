from lib.read.lists import file_to_list
from lib.types.pyroclastic import Pyroclastic

iter = file_to_list("data/day17.txt")
p = Pyroclastic(next(iter))
p.drop_rocks(2022)
print(p.max_height)

iter = file_to_list("data/day17.txt")
p = Pyroclastic(next(iter))
p.drop_rocks(1000000000000)
print(p.max_height)