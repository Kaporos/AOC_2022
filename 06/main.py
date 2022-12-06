MARKER_LENGTH = 4 # 14 for part two
with open("input") as f:
    content = f.read()
    pointer = 0
    chars = []
    while len(chars) < MARKER_LENGTH and pointer < (len(content)):
        char = content[pointer]
        if not char in chars:
            chars.append(char)
            pointer += 1
        else:
            pointer -= (len(chars) - 1)
            chars = []
    print(pointer)

