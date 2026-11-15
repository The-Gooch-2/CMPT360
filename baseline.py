

def cover(O, C, S, R):
    e = []
    for i in range(0,len(S)-1):
        e.append((S[i]-R[i], S[i]+R[i]))

    SC = []
    for i in range(0, len(e)-1):
        SC[i] = []
        for cactus in C:
            if e[i][0] <= cactus and cactus <= e[i][1]:
                SC[i].append(cactus)

    OC = []
    for i in range(0, len(e)-1):
        OC[i] = []
        for tree in T:
            if e[i][0] <= tree and tree <= e[i][1]:
                OC[i].append(tree)

    trees = O
    counter = 0
    solution = []
    while not trees:
        for i in range(0, len(SC)-1):
            if len(SC[i]) <= counter:
                solution.append(S[i])
                for tree in OC[i]:
                    trees.remove(tree)


        counter+=1


    return solution