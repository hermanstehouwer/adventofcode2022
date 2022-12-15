from lib.read.lists import file_to_list
from lib.types.beacon import Beacon

iter = file_to_list("data/day15.txt")
beacon = Beacon(iter)
print(beacon.excluded_on_line(2000000))
print(beacon.locate_beacon_tuning_frequency(4000000))