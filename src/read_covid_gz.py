import gzip
import sys

if len(sys.argv) != 2:
    print(f"#usage: python {sys.argv[0]} [file]")
    sys.exit()
#file_name = "covid19.fasta.gz"
file_name = sys.argv[1]

data = dict()

#with gzip.open(file_name, 'rb') as handle:
with gzip.open(file_name, 'rt') as handle:
    for line in handle:
        #line = line.decode("utf-8")
        if line.startswith(">"):
            continue
        for base in line.strip():
            if base not in data:
                data[base] = 0
            data[base] += 1

print(data)
