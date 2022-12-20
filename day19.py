from multiprocessing import Pool

from lib.read.lists import file_to_list
from lib.types.blueprint import BluePrint


def apply1(line):
    print(line)
    res = BluePrint(line).quality_level(24)
    print(res)


def apply2(line):
    print(line)
    res = BluePrint(line).quality_level(32)
    print(res)


if __name__ == "__main__":
    iter = file_to_list("data/day19.txt")
    lines = list(iter)
    results = []

    with Pool(8) as p:
        results = 0
        for result in p.map(apply1, lines):
            if result:
                results += result
        print(results)

    with Pool(8) as p:
        results = 1
        for result in p.map(apply2, lines[:3]):
            if result:
                results *= result
        print(results)


