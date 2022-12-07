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
        l = line.split(" ")
        match l[0]:
            case "$":
                match l[1]:
                    case "cd":
                        if l[2] == "/":
                            curr_dir = root
                        elif l[2] == "..":
                            curr_dir = curr_dir.parent
                        else:
                            curr_dir = curr_dir.subdirs[l[2]]
                    case "ls":
                        pass
            case "dir":
                dir_name = l[1]
                new_dir = Directory(name=dir_name, files=[], subdirs={}, parent=curr_dir)
                curr_dir.subdirs[dir_name] = new_dir
                dirs.append(new_dir)
            case _:
                file_size = int(l[0])
                file_name = l[1]
                curr_dir.files.append(File(file_size, file_name))
    return dirs


def filter_directory(d: Directory) -> bool:
    return d.calc_size() < 100000
