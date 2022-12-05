top3 = [0, 0, 0]
with open("dane.in") as file:
    s = 0
    for line in file:
        line = line.strip()
        if line == "":
            top3[top3.index(min(top3))] = max(min(top3), s)
            s = 0
        else:
            s += int(line)
    top3[top3.index(min(top3))] = max(min(top3), s)
    print(top3)
    print(sum(top3))
