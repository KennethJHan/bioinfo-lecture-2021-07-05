import sys

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [n1]")
    sys.exit()

n1 = int(sys.argv[1])

result = "neither 3,7"

if n1 % 3 == 0 and n1 % 7 == 0:
    result = "3,7"
elif n1 % 3 == 0:
    result = "3"
elif n1 % 7 == 0:
    result = "7"

print(result)

