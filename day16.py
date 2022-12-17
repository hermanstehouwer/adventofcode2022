from lib.read.lists import file_to_list
from lib.types.valves import Pipes

iter = file_to_list("data/day16.txt")
pipes = Pipes(iter)
print(pipes.max_pressure_released(30))
print(pipes.max_pressure_released(26, True))
