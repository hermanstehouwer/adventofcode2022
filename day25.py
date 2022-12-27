from lib.read.lists import file_to_list
from lib.transform.snafu import snafu2int, int2snafu

iter = file_to_list("data/day25.txt")
snafu = sum(map(snafu2int, iter))
print(int2snafu(snafu))
