from lib.read.lists import file_to_list
from lib.types.grove_coordinates import GroveCoordinates

iter = file_to_list("data/day20.txt")
grove = GroveCoordinates(iter)
grove.mix_all()
print(sum([grove.value_of_coord(0, x) for x in [1000, 2000, 3000]]))

iter = file_to_list("data/day20.txt")
grove = GroveCoordinates(iter, decryption_key=811589153)
grove.mix_all(times=10)
print(sum([grove.value_of_coord(0, x) for x in [1000, 2000, 3000]]))
