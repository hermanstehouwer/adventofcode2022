from lib.read.lists import file_to_list
from lib.transform.transform import add_lists_seperated_empty_line, to_int

values = add_lists_seperated_empty_line(
                to_int(file_to_list("data/day1.txt"))
            )
vals = list(values)
vals.sort()

print(max(vals))
print(sum(vals[-3:]))