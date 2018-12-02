import sys
import time
from collections import Counter

start = time.time()

with open(sys.argv[1]) as f:
    li = (line.strip() for line in f)
    se = [set(Counter(l).values()) for l in li]

    twos  = len([s for s in se if 2 in s])
    thres = len([s for s in se if 3 in s])

    print("{0} * {1} = {2}".format(twos, thres, twos * thres))

stop = time.time()

print("Elapsed time: {:.4f} s".format(stop-start))

