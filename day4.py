from lib.read.lists import file_to_list
from lib.transform.transform import to_range, split_two, overlap_all_sets, overlap_partial_sets

a = map(lambda x: map(to_range, x),
        split_two(file_to_list("data/day4.txt"), split=","))
b = filter(overlap_all_sets, a)
print(len(list(b)))

aa = map(lambda x: map(to_range, x),
        split_two(file_to_list("data/day4.txt"), split=","))
bb = filter(overlap_partial_sets, aa)
print(len(list(bb)))