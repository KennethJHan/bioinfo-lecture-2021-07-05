s = "ATGTTATAG"
s_rev = s[::-1]
print(s)
print(s_rev)

for i in range(len(s)):
    print(f"{s[i]}{s_rev[i]}")
