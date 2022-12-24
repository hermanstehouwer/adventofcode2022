from lib.read.lists import file_to_list
from lib.types.blizzard import Blizzard

iter = file_to_list("data/day24.txt")
blizzard = Blizzard(iter)
print(blizzard.lenght_fastest_path())
print(blizzard.lenght_fastest_path(forgot_snacks=True))
