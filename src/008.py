
import sys

n = int(sys.argv[1])
val = 1

while n > 0:
    val *= n
    n -= 1
print(val)

