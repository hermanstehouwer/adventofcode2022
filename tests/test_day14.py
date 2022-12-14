from lib.types.regiolith import Regiolith

lines = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""".split("\n")


def test_part1():
    rl = Regiolith(iter(lines))
    assert rl.simulate_pour() == 24


def test_part2():
    rl = Regiolith(iter(lines))
    assert rl.simulate_pour(floor=True) == 93
