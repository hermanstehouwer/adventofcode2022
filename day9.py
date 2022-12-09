from lib.read.lists import file_to_list
from lib.types.rope_bridge import RopeBridge

iter = file_to_list("data/day9.txt")
rope_bridge = RopeBridge()
rope_bridge.do_moves(iter)
print(rope_bridge.number_of_fields_visited_by_tail())

iter = file_to_list("data/day9.txt")
rope_bridge = RopeBridge(length_rope=10)
rope_bridge.do_moves(iter)
print(rope_bridge.number_of_fields_visited_by_tail())
