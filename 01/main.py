
with open("input","r") as f:
    content = f.read()
    elves = content.split("\n\n")
    elvesList = []
    for (i, elve) in enumerate(elves):
        calories = sum([int(x) for x in elve.split("\n") if x.isnumeric()])
        elvesList.append(calories)
    elvesList.sort(reverse=True)
    print(elvesList[:3])
    print(sum(elvesList[:3]))

# Not 195137