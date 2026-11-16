def cover(O, C, S, R):
    e = []
    for i in range(0,len(S)):
        e.append((S[i]-R[i], S[i]+R[i]))
 
    SC = []
    for i in range(0, len(e)):
        SC.append([])
        for cactus in C:
            if e[i][0] <= cactus and cactus <= e[i][1]:
                SC[i].append(cactus)

    SO = []
    for i in range(0, len(e)):
        SO.append([])
        for tree in O:
            if e[i][0] <= tree and tree <= e[i][1]:
                SO[i].append(tree)

    trees = O[:]
    counter = 0
    solution = []
    while len(trees) > 0:
        for i in range(0, len(SC)):
            if len(SC[i]) == counter:
                solution.append(S[i])
                for tree in SO[i]:
                    print(trees)
                    if tree in trees:
                        trees.remove(tree)
                    if not trees:
                        return solution  
        counter += 1

a1 = [2,6,11]
a2 = [4,8,14]
a3 = [3,7,12]
a4 = [3, 2, 1]

print(cover(a1, a2, a3, a4))