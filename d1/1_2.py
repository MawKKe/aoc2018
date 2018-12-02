import sys
import time
from itertools import cycle

def run(fn):
    with open(fn) as f:
        li = cycle([(l[0], int(l[1:])) for l in (line.strip() for line in f)])
        s = 0
        vals = set([s])
        for sig, N in li:
            s = s + N if sig == '+' else s - N
            if s in vals:
                return s
            else:
                vals.add(s)

    return None


start = time.time()

res = run(sys.argv[1])

stop  = time.time()

if res:
    print("Found:", res)
else:
    print("Not found :(")

print("Elapsed time: {:.4f} s".format(stop-start))
