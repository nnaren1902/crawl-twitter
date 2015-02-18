

total_count = {}
with open("../output/count.txt") as f:
    for line in f:
        (key, val) = line.split("\t")
        total_count[str(key)] = int(val)
       
