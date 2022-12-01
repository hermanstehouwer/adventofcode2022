from pathlib import Path
from typing import List, AnyStr


def file_to_list(file: Path) -> List[AnyStr]:
    for line in open(file, "r"):
        yield line.strip()

