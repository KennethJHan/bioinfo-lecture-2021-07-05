file_name = "read_sample.txt"

#with open(file_name, "r") as handle:
#    for line in handle:
#        print(line.strip())

with open(file_name, "r") as handle:
    lines = handle.readlines()
    for line in lines:
        print(line.strip())

#handle = open(file_name, "r")
#for line in handle:
#    print(line.strip())
#handle.close()

handle = open(file_name, "r")
lines = handle.readlines()
for line in lines:
    print(line.strip())
handle.close()

