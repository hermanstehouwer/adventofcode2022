from lib.read.lists import file_to_list
from lib.transform.transform import split_two
from lib.types.rock_paper_scissors import score_round, iter_to_RPS, iter_to_new_strat


score = 0
for round in iter_to_RPS(split_two(file_to_list("data/day2.txt"))):
    score += score_round(round[0], round[1])
print(score)

score = 0
for round in iter_to_new_strat(iter_to_RPS(split_two(file_to_list("data/day2.txt")))):
    score += score_round(round[0], round[1])
print(score)
