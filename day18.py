from lib.read.lists import file_to_list
from lib.types.droplet import Droplet

iter = file_to_list("data/day18.txt")
droplet = Droplet(iter)
print(droplet.calculate_sides())
print(droplet.calculate_surface())
