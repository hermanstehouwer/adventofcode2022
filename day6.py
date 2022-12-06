from lib.process.tuning import lockon_tuning

with open("data/day6.txt") as f:
    line = f.readline()
line = line.rstrip()

print(lockon_tuning(iter(line)))

print(lockon_tuning(iter(line), target_lenght=14))