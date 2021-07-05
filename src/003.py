import sys

if len(sys.argv) != 3:
    print(f"#usage: python {sys.argv[0]} [n1] [n2]")
    sys.exit()

n1 = int(sys.argv[1])
n2 = int(sys.argv[2])

print(f"{n1} + {n2} = {n1+n2}")
print(f"{n1} - {n2} = {n1-n2}")
print(f"{n1} x {n2} = {n1*n2}")
print(f"{n1} ÷ {n2} = {n1/n2}")
print(f"{n1} % {n2} = {n1%n2}")
print(f"{n1} ** {n2} = {n1**n2}")

