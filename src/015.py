import sys

if len(sys.argv) != 2:
    print(f"python {sys.argv[0]} [num]")
    sys.exit(1)

try:
    num = int(sys.argv[1])
except ValueError as err:
    print(f"{err}, your input: {sys.argv[1]}")
    sys.exit(3)
try:
    res = 10 / num
except ZeroDivisionError as err:
    print(err)
    sys.exit(2)
print(res)
