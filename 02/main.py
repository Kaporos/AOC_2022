scores = {
    "X": 1,
    "Y": 2,
    "Z": 3
}
wins = {
    "A": "Y",
    "B": "Z",
    "C": "X"
}
eqs = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}
with open("input", "r") as f:
    score = 0
    for line in f:
        opp,me = line.strip().split()
        me = me.replace("Z","G").replace("X","P").replace("Y","E")
        if me == "G":
            me = wins[opp]
        if me == "E":
            me = eqs[opp]
        if me == "P":
            for x in wins.values():
                if x != wins[opp] and x != eqs[opp]:
                    me = x
        score += scores[me]
        if me == wins[opp]:
            score += 6
        if me == eqs[opp]:
            score += 3          
    print(score)