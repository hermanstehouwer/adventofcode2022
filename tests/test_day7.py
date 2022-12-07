from lib.read.lists import file_to_list
from lib.types.filesystem import iter_and_parse, filter_directory


def test_part_one():
    iter = file_to_list("tests/data/day7.txt")
    dirs = iter_and_parse(iter)
    filtered = filter(filter_directory, dirs)
    assert sum([f.calc_size() for f in filtered]) == 95437

def test_part_two():
    iter = file_to_list("tests/data/day7.txt")
    dirs = iter_and_parse(iter)
    dir_sizes = [f.calc_size() for f in dirs]
    size_of_root = max(dir_sizes)
    minimum_size = 30000000 - (70000000 - size_of_root)
    assert min([x for x in dir_sizes if x > minimum_size]) == 24933642
