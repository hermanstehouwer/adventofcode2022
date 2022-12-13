from lib.read.lists import file_to_list
from lib.transform.distress import process_and_sum, prep_pairs, list_to_pairs, sort_and_decode

iter = file_to_list("data/day13.txt")
print(process_and_sum(prep_pairs(list_to_pairs(iter))))

iter = file_to_list("data/day13.txt")
print(sort_and_decode(iter))