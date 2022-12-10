from typing import AnyStr, Iterator, List

interesting_cycles = [20, 60, 100, 140, 180, 220]


class Signal():
    X: int
    cycle: int
    signal: int
    buffer: List[AnyStr]

    def __init__(self):
        self.X = 1
        self.cycle = 1
        self.signal = 0
        self.buffer = []

    def process_instruction(self, instruction: AnyStr) -> None:
        self.draw()
        if self.cycle in interesting_cycles:
            self.signal += self.cycle * self.X
        match instruction.split():
            case "noop": pass
            case "addx", x:
                x = int(x)
                self.X += x
        self.cycle += 1

    def process_instructions(self, instructions: Iterator[AnyStr]) -> None:
        def preprocess(it):
            for i in it:
                match i:
                    case "noop": yield i
                    case _:
                        yield "noop"
                        yield i
        for instruction in preprocess(instructions):
            self.process_instruction(instruction)

    def draw(self):
        self.buffer.append("#") if abs(self.X - ((self.cycle-1) % 40)) <= 1 else self.buffer.append(".")
        if len(self.buffer) == 40:
            print("".join(self.buffer))
            self.buffer = []
