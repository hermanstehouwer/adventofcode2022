from lib.read.lists import file_to_list
from lib.types.trees import lines_to_ints, visible_trees, max_scenic_score

iter = file_to_list("data/day8.txt")
trees = lines_to_ints(iter)
print(visible_trees(trees))
print(max_scenic_score(trees))