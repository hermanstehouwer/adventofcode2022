from lib.read.lists import file_to_list
from lib.types.grove_planting import GrovePlanting

iter = file_to_list("data/day23.txt")
grove = GrovePlanting(iter)
grove.rounds(10)
print(grove.count_empty_ground())

iter = file_to_list("data/day23.txt")
grove = GrovePlanting(iter)
print(grove.rounds(-1))