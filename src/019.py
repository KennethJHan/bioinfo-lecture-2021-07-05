import sys

# with open("hahaha.txt", 'r') as handle:
#     data = handle.readlines()
#
# print(data)

try:
    with open("hahaha.txt", 'r') as handle:
        data = handle.readlines()
except FileNotFoundError as err:
    print(err)
    sys.exit()

print(data)
