from lib.read.lists import file_to_list
from lib.types.signal_strenght import Signal


def test_signal_strength():
    iter = file_to_list("tests/data/day10.txt")
    signal = Signal()
    signal.process_instructions(iter)
    assert signal.signal == 13140

