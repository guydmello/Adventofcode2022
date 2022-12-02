with open("moves.txt", "r") as calories:
	lines = calories.readlines()

lines = [s.strip('\n') for s in lines] 
lines = [s.replace('\n', '') for s in lines]

score = 0
for l in lines:
    opp, you = l.split()

    if you == "X":
        if opp == "C":
            score += 6
        if opp == "A":
            score += 3
        score += 1

    if you == "Y":
        if opp == "A":
            score += 6
        if opp == "B":
            score += 3
        score += 2

    if you =="Z":
        if opp == "B":
            score += 6
        if opp == "C":
            score += 3
        score += 3

print(score)


score2 = 0
for l in lines:
    opp, you = l.split()

    if you == "X":
        if opp == "A":
            score2 += 3
        if opp == "B":
            score2 += 1
        if opp == "C":
            score2 += 2
        
        score2 += 0

    if you == "Y":
        if opp == "A":
            score2 += 1
        if opp == "B":
            score2 += 2
        if opp == "C":
            score2 += 3
        score2 += 3

    if you =="Z":
        if opp == "A":
            score2 += 2
        if opp == "B":
            score2 += 3
        if opp == "C":
            score2 += 1
        score2 += 6

print(score2)


# index = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

# # print(lines)

# results = []

# for i in lines:

#     # A beats Z
#     if (i[0] == 'A' and i[1] == 'Z'):
#         results.append(index.get(i[1]))
#     # A ties with X
#     elif (i[0] == 'A' and i[1] == 'X'):
#         results.append((index.get(i[1]) + 3))
#     # A loses to y
#     elif (i[0] == 'A' and i[1] == 'Y'):
#         results.append((index.get(i[1]) + 6))
#     # b beats x
#     elif (i[0] == 'B' and i[1] == 'X'):
#         results.append(index.get(i[1]))
        
#     # b ties with Y
#     elif (i[0] == 'B' and i[1] == 'Y'):
#         results.append((index.get(i[1]) + 3))

#     # b loses with Z
#     elif (i[0] == 'B' and i[1] == 'Z'):
#         results.append((index.get(i[1]) + 6))

#     # c beats y
#     elif (i[0] == 'C' and i[1] == 'Y'):
#         results.append(index.get(i[1]))

#     # C ties with Z
#     elif (i[0] == 'C' and i[1] == 'Z'):
#         results.append((index.get(i[1]) + 3))
    
#     # C LOSES with X
#     elif (i[0] == 'C' and i[1] == 'X'):
#         results.append(index.get(i[1]))

# print(results)

