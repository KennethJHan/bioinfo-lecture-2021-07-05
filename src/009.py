

def greet():
    print("Hello, Bioinformatics")

def greet1(name: str) -> None:
    print(f"Hello, {name}")

def greet2(num: int) -> int:
    return num * 2

greet()
ret1 = greet1("ken")
print(ret1)

ret2 = greet2(3)
print(ret2)


