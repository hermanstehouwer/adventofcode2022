from lib.read.lists import file_to_list
from lib.transform.transform import iter_split_middle, iter_tuple_to_unique_character, iter_char_to_priority, \
    iter_group

print(sum(iter_char_to_priority(iter_tuple_to_unique_character(iter_split_middle(file_to_list("data/day3.txt"))))))

print(sum(iter_char_to_priority(iter_tuple_to_unique_character(iter_group(file_to_list("data/day3.txt"))))))
