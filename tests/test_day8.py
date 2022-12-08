from lib.types.trees import lines_to_ints, visible_trees, max_scenic_score

test_trees = """30373
25512
65332
33549
35390""".split("\n")


def test_number_of_visible_trees():
    trees = lines_to_ints(test_trees)
    assert visible_trees(trees) == 21


def test_best_scenic_score():
    trees = lines_to_ints(test_trees)
    assert max_scenic_score(trees) == 8
