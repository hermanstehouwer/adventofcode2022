from lib.read.lists import file_to_list
from lib.transform.transform import iter_group, split_middle, char_to_priority, tuple_to_unique_character

print(sum(
    map(char_to_priority,
        map(tuple_to_unique_character,
            (map(split_middle, file_to_list("data/day3.txt")))))))

print(sum(
    map(char_to_priority,
        map(tuple_to_unique_character,(iter_group(file_to_list("data/day3.txt")))))))
