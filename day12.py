from lib.read.lists import file_to_list
from lib.types.climbing import Climbing

iter = file_to_list("data/day12.txt")
climber = Climbing(iter)
print(climber.lenght_shortest_path_to_signal())
print(climber.lenght_scenic_path_to_signal())