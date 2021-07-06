import sys

with open("hahaha.txt", 'r') as handle:
    data = handle.readlines()

print(data)

try:
    with open("hahaha.txt", 'r') as handle:
        data = handle.readlines()
except FileNotFoundError as err:
    print("파일이 없음")
    sys.exit()

print(data)
