seq = "AGTTTATAG"

for i in range(len(seq)):
    s = seq[i:i+2]
    print(i, s, s=="TT")
    #if s == "TT":
    #    print(i)


