def answer(PART_TWO=False):
    with open("input") as f:
        lines = f.readlines()
        stacks = [[] for x in range(9)]
        for line in lines:
            if not "[" in line:
                if "move" in line:
                    line = line.split()
                    quantity, origin, dest = int(line[1]), int(line[3])-1, int(line[5])-1
                    for x in range(quantity):
                        item = stacks[origin].pop(0)
                        stacks[dest].insert(x if PART_TWO else 0,item)
            else:
                for x in range(9):
                    letter = line[1+x*4:2+x*4]
                    if letter != " ":
                        stacks[x].append(letter)
        msg = ""
        for (i,stack) in enumerate(stacks):
            first = stack[0]
            msg += first 
        print(msg)
        
print("PART 1")
answer(False)
print("PART 2")
answer(True)