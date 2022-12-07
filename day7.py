from lib.read.lists import file_to_list
from lib.types.filesystem import iter_and_parse, filter_directory

iter = file_to_list("data/day7.txt")
dirs = iter_and_parse(iter)
filtered = filter(filter_directory, dirs)
print(sum([f.calc_size() for f in filtered]))

dir_sizes = [f.calc_size() for f in dirs]
size_of_root = max(dir_sizes)
minimum_size = 30000000 - (70000000 - size_of_root)
print(min([x for x in dir_sizes if x > minimum_size]))