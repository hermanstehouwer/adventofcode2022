from typing import AnyStr, List, Iterable, Dict, Tuple


class MonkeyTree:
    def __init__(self, it: Iterable[AnyStr]):
        self.tree: Dict[AnyStr, List[AnyStr]] = dict()
        for line in it:
            a, b = line.split(": ")
            self.tree[a] = b.split(" ")

    def calculate_value(self, node: AnyStr = "root") -> int:
        match self.tree[node]:
            case [a]: return int(a)
            case [a, "+", b]: return self.calculate_value(a) + self.calculate_value(b)
            case [a, "-", b]: return self.calculate_value(a) - self.calculate_value(b)
            case [a, "/", b]: return self.calculate_value(a) // self.calculate_value(b)
            case [a, "*", b]: return self.calculate_value(a) * self.calculate_value(b)

    def find_human_value_start(self) -> int:
        hmn, comp = self.get_hmn_comp("root")
        return self.find_human_value_recurse(hmn, self.calculate_value(comp))

    def find_human_value_recurse(self, node: AnyStr, must_equal: int) -> int:
        if node == "humn": return must_equal
        hmn, comp = self.get_hmn_comp(node)
        match self.tree[node][1]:
            case "+": return self.find_human_value_recurse(hmn, must_equal - self.calculate_value(comp))
            case "-":
                if hmn == self.tree[node][0]:
                    return self.find_human_value_recurse(hmn, must_equal + self.calculate_value(comp))
                return self.find_human_value_recurse(hmn, self.calculate_value(comp) - must_equal)
            case "*": return self.find_human_value_recurse(hmn, must_equal // self.calculate_value(comp))
            case "/":
                if hmn == self.tree[node][0]:
                    return self.find_human_value_recurse(hmn, must_equal * self.calculate_value(comp))
                return self.find_human_value_recurse(hmn, self.calculate_value(comp) // must_equal)

    def human_in(self, node: AnyStr) -> bool:
        if node == "humn": return True
        if len(self.tree[node]) == 1: return False
        return self.human_in(self.tree[node][0]) or self.human_in(self.tree[node][2])

    def get_hmn_comp(self, node: AnyStr) -> Tuple[AnyStr, AnyStr]:
        content = self.tree[node]
        if self.human_in(content[0]):
            return content[0], content[2]
        return content[2], content[0]
