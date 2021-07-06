class ValueCalculator:
    def __init__(self, val: str):
        self.val = val

    def __add__(self, other):
        return self.val + other.val

def Add(n1, n2):
    return n1 + n2

if __name__ == "__main__":
    print('hi')

