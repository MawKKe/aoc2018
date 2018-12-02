import sys
import time

# Usage: python3 <filename> input.txt

start = time.time()

with open(sys.argv[1]) as f:
    li = (line.strip() for line in f)
    s = 0
    for l in li:
        sig, N = l[0], int(l[1:])
        if sig == "+":
            s += N
        else:
            s -= N
    print(s)

stop = time.time()

print("Elapsed time: {:.4f} s".format(stop-start))

# You could also do something stupid like this:
#
#   print(eval(("0" + open(sys.argv[1]).read().replace('\n',''))))
#

# Or even something like this in bash:
#
#   (( x = $(cat <(echo "0") input.txt) )); echo $x
#
