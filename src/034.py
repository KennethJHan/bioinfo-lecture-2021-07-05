data = [3, 1, 1, 2, 0, 0, 2, 3, 3]
print(min(data))
print(max(data))

cnt = dict()
for elem in data:
    if elem not in cnt:
        cnt[elem] = 0
    cnt[elem] += 1
print(cnt)
