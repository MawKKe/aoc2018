from collections import Counter
from itertools import combinations
import sys
import time

# correct was: wlkigsqyfecjqqmnxaktdrhbz

start = time.time()

with open(sys.argv[1]) as f:
    co = combinations([line.strip() for line in f], 2)
    for a,b in co:
        if sum(x != y for x, y in zip(a,b)) != 1:
            continue

        print("found:\n{0}\n{1}\n".format(a,b))

        # get common elements, character-by-character, but NOT not in sorted form.
        r = ''.join(x for x,y in zip(a,b) if x == y)

        print("common:\n{0}".format(r))

        break

stop = time.time()

print("time:", stop-start)
print("Elapsed time: {:.4f} s".format(stop-start))

