with open("input") as f:
    total = 0
    for line in f:
        line = line.strip()
        if len(line) == 0:
            continue
        first,second = line.split(",")
        first_start, first_end = first.split("-")
        second_start, second_end = second.split("-")
        first_start, first_end, second_start, second_end = int(first_start), int(first_end), int(second_start), int(second_end)
        if (first_start >= second_start and first_end <= second_end) or (second_start >= first_start and second_end <= first_end):
            total += 1
    print(total)


## PART TWO

with open("input") as f:
    total = 0
    for line in f:
        line = line.strip()
        if len(line) == 0:
            continue
        first,second = line.split(",")
        first_start, first_end = first.split("-")
        second_start, second_end = second.split("-")
        first_start, first_end, second_start, second_end = int(first_start), int(first_end), int(second_start), int(second_end)
        if (first_start >= second_start and first_start <= second_end) or (second_start >= first_start and second_start <= first_end):
            total += 1
    print(total)