from lib.types.monkeys import Monkeys
from pytest import fixture

@fixture
def monkeys():
    monkeys = Monkeys()
    monkeys.add_monkey([79, 98], lambda x: x * 19, 23, 2, 3)
    monkeys.add_monkey([54, 65, 75, 74], lambda x: x + 6, 19, 2, 0)
    monkeys.add_monkey([79, 60, 97], lambda x: x * x, 13, 1, 3)
    monkeys.add_monkey([74], lambda x: x + 3, 17, 0, 1)
    yield monkeys


def test_simian_shenanigans(monkeys):
    monkeys.execute_rounds(20)
    assert monkeys.monkey_business() == 10605


def test_very_worried(monkeys):
    monkeys.execute_rounds(10000, very_worried=True)
    assert monkeys.monkey_business() == 2713310158
