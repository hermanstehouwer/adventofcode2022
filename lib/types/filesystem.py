from dataclasses import dataclass
from typing import Iterator, AnyStr, List, Dict


@dataclass()
class File:
    size: int
    name: AnyStr


@dataclass
class Directory:
    name: AnyStr
    files: List['File']
    subdirs: Dict[AnyStr, 'Directory']
    parent: 'Directory'

    def calc_size(self) -> int:
        return sum([f.size for f in self.files]) + sum([d.calc_size() for d in self.subdirs.values()])


def iter_and_parse(iter: Iterator[AnyStr]) -> List[Directory]:
    root: Directory = Directory(name="/", files=[], subdirs={}, parent=None)
    dirs: List[Directory] = [root]
    curr_dir: Directory = None # Assume: first command is cd /
    for line in iter:
        match line.split(" "):
            case ["$", "cd", "/"]:
                curr_dir = root
            case ["$", "cd", ".."]:
                curr_dir = curr_dir.parent
            case ["$", "cd", tgt_dir]:
                curr_dir = curr_dir.subdirs[tgt_dir]
            case ["$", "ls"]:
                pass
            case ["dir", dir_name]:
                dirs.append(Directory(name=dir_name, files=[], subdirs={}, parent=curr_dir))
                curr_dir.subdirs[dir_name] = dirs[-1]
            case [file_size, file_name]:
                curr_dir.files.append(File(int(file_size), file_name))
    return dirs


def filter_directory(d: Directory) -> bool:
    return d.calc_size() < 100000
