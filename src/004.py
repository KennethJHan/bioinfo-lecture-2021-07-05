import sys

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [num]")
    sys.exit()

num = int(sys.argv[1])

result = "odd"

if num % 2 == 0:
    result = "even"

print(result)

