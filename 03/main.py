def get_score(letter):
    d = letter.lower()
    uppercase = letter != d
    nbr = ord(d) - 96
    if uppercase:
        nbr += 26
    return nbr

with open("input") as f:
    total = 0
    lines = f.readlines()
    for (i,line) in enumerate(lines):
        line = line.strip()
        length = len(line)
        first = line[:length//2]
        sec = line[length//2:]
        dup = [x for x in first if x in sec]
        total += get_score(dup[0])
    print("PART ONE: ",total)
        
## part two

import numpy as np
with open("input") as f:
    total = 0
    lines = np.asarray(f.readlines())
    u = np.array_split(lines, len(lines)/3)
    for group in u:
        common = [x for x in group[0].strip() if x in group[1] and x in group[2]]
        score = get_score(common[0])
        total += score
    print("PART TWO: ", total)