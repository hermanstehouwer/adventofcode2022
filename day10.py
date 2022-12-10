from lib.read.lists import file_to_list
from lib.types.signal_strenght import Signal

iter = file_to_list("data/day10.txt")
signal = Signal()
signal.process_instructions(iter)
print(signal.signal)